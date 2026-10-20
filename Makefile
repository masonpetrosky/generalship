PYTHON ?= python3

.PHONY: check reproduce estimate-evaluation commander-ratings estimate-evaluation-v2 commander-ratings-v2 strength-imputation commander-ratings-v3 rating-uncertainty strength-imputation-v2 commander-ratings-v4 napoleonic-methods packet review-bundle
check:
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) -m generalship check
	$(PYTHON) -m generalship.napoleonic_boundaries
	$(PYTHON) -m generalship.napoleonic_authority
	$(PYTHON) -m generalship.napoleonic_inventory
	$(PYTHON) -m generalship.napoleonic_measurement
	$(PYTHON) -m generalship.napoleonic_benchmark

reproduce:
	$(PYTHON) -m generalship.napoleonic_boundaries --write
	$(PYTHON) -m generalship.napoleonic_authority --write
	$(PYTHON) -m generalship.napoleonic_inventory --write
	$(PYTHON) -m generalship.napoleonic_measurement --write
	$(PYTHON) -m generalship.napoleonic_benchmark --write
	$(PYTHON) -m generalship build

napoleonic-methods:
	$(PYTHON) -m generalship napoleonic-methods

estimate-evaluation:
	$(PYTHON) -m generalship estimate-evaluate

commander-ratings:
	$(PYTHON) -m generalship commander-ratings

estimate-evaluation-v2:
	$(PYTHON) -m generalship estimate-evaluate --version 2

commander-ratings-v2: estimate-evaluation-v2
	$(PYTHON) -m generalship commander-ratings --version 2

strength-imputation:
	$(PYTHON) -m generalship strength-imputation

commander-ratings-v3:
	$(PYTHON) -m generalship commander-ratings --version 3

rating-uncertainty:
	$(PYTHON) -m generalship rating-uncertainty --version 3

strength-imputation-v2:
	$(PYTHON) -m generalship strength-imputation --version 2

commander-ratings-v4:
	$(PYTHON) -m generalship commander-ratings --version 4

packet:
	$(PYTHON) -m generalship packet TN003

review-bundle:
	$(PYTHON) scripts/prepare_shiloh_review.py
