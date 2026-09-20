PYTHON ?= python3

.PHONY: check reproduce packet review-bundle
check:
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) -m generalship check

reproduce:
	$(PYTHON) -m generalship build

packet:
	$(PYTHON) -m generalship packet TN003

review-bundle:
	$(PYTHON) scripts/prepare_shiloh_review.py
