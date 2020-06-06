.PHONY: list activate install update \
		flake mypy mypy-context black black-check checks \
		plot, run-solver, run-exp, test

.DEFAULT_GOAL := activate

SHELL := /bin/bash

PIPENV_RUN = PYTHONPATH=${PYTHONPATH}:${PWD} pipenv run

ROOT_PYTHON_PACKAGES = binpacking tests


list:
	# Listing of available make targets
	@(grep -oe '^[[:lower:][:digit:]_\-]\{1,\}:' Makefile | tr -d ':' | uniq)

# PIPENV and dependencies

activate:
	pipenv shell

install:
ifneq ($(DEV_PACKAGE),)
	$(PIPENV_RUN) pipenv install -d $(DEV_PACKAGE) $(ARGS)
else
ifneq ($(PACKAGE),)
	$(PIPENV_RUN) pipenv install $(PACKAGE) $(ARGS)
else
	$(PIPENV_RUN) pipenv install -d $(ARGS)
endif
endif

update:
	$(PIPENV_RUN) pipenv update $(PACKAGE) $(ARGS)

# Code checks and formatting

flake: CONFIG ?= --config .config/flake8.cfg
flake:
	$(PIPENV_RUN) flake8 $(CONFIG) $(ARGS)

mypy: CONFIG ?= --config-file .config/mypy.cfg
mypy:
	$(PIPENV_RUN) mypy $(ROOT_PYTHON_PACKAGES) $(CONFIG) $(ARGS)

mypy-context: # show error context not used as default as it can be a bit verbose with many errors
	make mypy ARGS="--show-error-context $(ARGS)"

black: CONFIG ?= --config .config/black.cfg
black:
	$(PIPENV_RUN) black $(ROOT_PYTHON_PACKAGES) $(CONFIG) $(ARGS)

black-check:
	make black ARGS="--check $(ARGS)"

checks:
	@(echo "FLAKE8..." && make flake > /dev/null 2>&1 && echo "          OK")
	@(echo "MYPY..." && make mypy > /dev/null 2>&1 && echo "          OK")
	@(echo "BLACK..." && make black-check > /dev/null 2>&1 && echo "          OK")

# Running code

plot:
	$(PIPENV_RUN) python -m binpacking.plot

run-solver:
	$(PIPENV_RUN) python -m binpacking.solver

run-exp:
	$(PIPENV_RUN) python -m binpacking.experimentations


# Running tests

test: TARGET ?= discover
test: TIME_CONSUMING ?= 0
test: # TARGET can be a path, as this replaces "/" by "." and ending ".py" by nothing
	RUN_TIME_CONSUMING_TESTS=$(TIME_CONSUMING) \
		$(PIPENV_RUN) python -m unittest $(patsubst %.py,%,$(subst /,.,$(TARGET))) $(ARGS)
