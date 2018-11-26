PYTHON := $(shell which python3.6)
ENV := $(CURDIR)/env
PIP := $(ENV)/bin/pip

$(ENV):
	$(PYTHON) -m venv env
	$(PIP_INSTALL) -U pip setuptools

deps: $(ENV)
	$(PIP) install --upgrade -r requirements/base.txt
