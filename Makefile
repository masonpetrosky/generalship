PYTHON ?= python3

.PHONY: check reproduce estimate-evaluation commander-ratings estimate-evaluation-v2 commander-ratings-v2 packet review-bundle
check:
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) -m generalship check

reproduce:
	$(PYTHON) -m generalship build

estimate-evaluation:
	$(PYTHON) -m generalship estimate-evaluate

commander-ratings:
	$(PYTHON) -m generalship commander-ratings

estimate-evaluation-v2:
	$(PYTHON) -m generalship estimate-evaluate --version 2

commander-ratings-v2: estimate-evaluation-v2
	$(PYTHON) -m generalship commander-ratings --version 2

packet:
	$(PYTHON) -m generalship packet TN003

review-bundle:
	$(PYTHON) scripts/prepare_shiloh_review.py
