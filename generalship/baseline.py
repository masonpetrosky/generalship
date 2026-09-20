"""Small transparent logistic baseline; predictions always hold out a campaign."""

from dataclasses import dataclass
from itertools import product
import math


def sigmoid(z):
    if z >= 0:
        return 1 / (1 + math.exp(-z))
    exp = math.exp(z)
    return exp / (1 + exp)


def advantage(own, opposing):
    if not all(math.isfinite(v) and v > 0 for v in (own, opposing)):
        raise ValueError("Strength must be finite, positive, and known")
    return (own - opposing) / (own + opposing)


@dataclass(frozen=True)
class LogisticModel:
    intercept: float
    slope: float

    def predict(self, x):
        return sigmoid(self.intercept + self.slope * x)


def fit_logistic(xs, ys, ridge=1.0):
    """Minimize sum(log loss) + ridge/2 * (intercept² + slope²).

    Newton's method with backtracking, a positive definite 2x2 Hessian,
    and an explicit convergence check. No stochastic optimizer or dependencies.
    """
    if not xs or len(xs) != len(ys) or not math.isfinite(ridge) or ridge <= 0:
        raise ValueError("Need paired observations and a positive finite ridge penalty")
    if any(not math.isfinite(x) or abs(x) > 1 for x in xs) or any(y not in (0, 1) for y in ys):
        raise ValueError("Invalid feature or binary outcome")
    a = b = 0.0

    def objective(a, b):
        total = ridge * (a*a + b*b) / 2
        for x, y in zip(xs, ys):
            z = a + b*x
            total += max(z, 0) + math.log1p(math.exp(-abs(z))) - y*z
        return total

    for _ in range(100):
        ga, gb, haa, hab, hbb = ridge*a, ridge*b, ridge, 0.0, ridge
        for x, y in zip(xs, ys):
            p = sigmoid(a + b*x)
            w = p * (1-p)
            ga += p-y
            gb += (p-y)*x
            haa += w
            hab += w*x
            hbb += w*x*x
        if max(abs(ga), abs(gb)) < 1e-9:
            return LogisticModel(a, b)
        determinant = haa*hbb - hab*hab
        da, db = (hbb*ga-hab*gb)/determinant, (haa*gb-hab*ga)/determinant
        step, current = 1.0, objective(a, b)
        while objective(a-step*da, b-step*db) > current - 1e-4*step*(ga*da+gb*db):
            step /= 2
            if step < 1e-12:
                # At machine precision, a sufficiently small Newton step is converged.
                if max(abs(da), abs(db)) < 1e-7:
                    return LogisticModel(a, b)
                raise ValueError("Logistic optimizer failed line search")
        a, b = a-step*da, b-step*db
    raise ValueError("Logistic optimizer did not converge")


def feature(record):
    strengths = record["strengths"]
    return advantage(*[(strengths[s]["low"] + strengths[s]["high"])/2 for s in ("US", "Confederate")])


def scores(predictions, key):
    if not predictions:
        raise ValueError("No predictions to score")
    brier, logloss = 0.0, 0.0
    for row in predictions:
        p, y = row[key], row["union_outcome"]
        if not math.isfinite(p) or not 0 <= p <= 1:
            raise ValueError("Invalid probability")
        brier += (p-y)**2
        p = min(1-1e-15, max(1e-15, p))
        logloss -= y*math.log(p) + (1-y)*math.log1p(-p)
    return {"brier": brier/len(predictions), "log_loss": logloss/len(predictions)}


def evaluate(records):
    eligible = [r for r in records if r["baseline_eligible"]]
    campaigns = sorted({r["campaign"] for r in eligible})
    if len(campaigns) < 3 or len(eligible) < 6:
        raise ValueError("Need at least 6 eligible battles from 3 campaigns")
    if len({r["source_result"] for r in eligible}) != 2:
        raise ValueError("Need both decisive outcome classes")
    predictions, folds = [], []
    for campaign in campaigns:
        train = [r for r in eligible if r["campaign"] != campaign]
        test = [r for r in eligible if r["campaign"] == campaign]
        xs, ys = [feature(r) for r in train], [int(r["source_result"] == "Union") for r in train]
        model = fit_logistic(xs, ys)
        prior = (sum(ys)+1)/(len(ys)+2)  # Laplace-smoothed, training rows only.
        folds.append({"held_out_campaign": campaign,
                      "train_battle_ids": sorted(r["battle_id"] for r in train),
                      "test_battle_ids": sorted(r["battle_id"] for r in test),
                      "intercept": model.intercept, "slope": model.slope})
        for row in test:
            p, y = model.predict(feature(row)), int(row["source_result"] == "Union")
            us, cs = row["strengths"]["US"], row["strengths"]["Confederate"]
            endpoints = [model.predict(advantage(u, c)) for u, c in product(
                (us["low"], us["high"]), (cs["low"], cs["high"]))]
            predictions.append({"battle_id": row["battle_id"], "name": row["name"],
                                "campaign": campaign, "union_outcome": y,
                                "p_union_win": p, "p_equal_odds": 0.5, "p_training_prior": prior,
                                "union_residual": y-p, "confederate_residual": p-y,
                                "strength_sensitivity_p_min": min(endpoints),
                                "strength_sensitivity_p_max": max(endpoints),
                                "interpretation": "out_of_campaign_predictive_residual_not_command_effect"})
    predictions.sort(key=lambda row: row["battle_id"])
    metrics = {name: scores(predictions, key) for name, key in
               [("strength_logistic", "p_union_win"), ("equal_odds", "p_equal_odds"),
                ("training_prior", "p_training_prior")]}
    campaign_metrics = {
        name: {metric: sum(scores([p for p in predictions if p["campaign"] == c], key)[metric]
                           for c in campaigns)/len(campaigns) for metric in ("brier", "log_loss")}
        for name, key in [("strength_logistic", "p_union_win"), ("equal_odds", "p_equal_odds"),
                          ("training_prior", "p_training_prior")]
    }
    return {"model_id": "strength-logistic-v1", "status": "exploratory_imported_data",
            "validation": "leave_one_campaign_out", "n_battles": len(eligible),
            "n_campaigns": len(campaigns), "ridge": 1.0,
            "battle_weighted_metrics": metrics, "campaign_weighted_metrics": campaign_metrics,
            "folds": folds, "predictions": predictions,
            "limitations": ["Conditional on decisive recorded outcomes and available strengths.",
                            "Same commanders and theaters can occur in multiple campaigns.",
                            "Strength endpoints vary held-out inputs with the fitted model fixed; these are not confidence intervals.",
                            "No commander attribution, partial pooling, causal effects, or career rankings yet."]}
