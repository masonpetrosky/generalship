PYTHON ?= python3

.PHONY: check reproduce packet
check:
	$(PYTHON) -m unittest discover -s tests -v
	$(PYTHON) -m generalship check

reproduce:
	$(PYTHON) -m generalship build

packet:
	$(PYTHON) -m generalship packet TN003
