PYTHON ?= python3

.PHONY: check reproduce estimate-evaluation commander-ratings packet review-bundle
check:
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) -m generalship check

reproduce:
	$(PYTHON) -m generalship build

estimate-evaluation:
	$(PYTHON) -m generalship estimate-evaluate

commander-ratings:
	$(PYTHON) -m generalship commander-ratings

packet:
	$(PYTHON) -m generalship packet TN003

review-bundle:
	$(PYTHON) scripts/prepare_shiloh_review.py
