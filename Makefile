MODULE := rdkit_step
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

.PHONY: help
help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

.PHONY: clean
clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


.PHONY: clean-build
clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.PHONY: clean-pyc
clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	find . -name '.pytype' -exec rm -fr {} +

.PHONY: lint
lint: ## check style with flake8
	black --check --diff $(MODULE) tests
	flake8 $(MODULE) tests

.PHONY: format
format: ## reformat with with yapf and isort
	black $(MODULE) tests

.PHONY: test
test: ## run tests quickly with the default Python
	py.test

.PHONY: converage
coverage: ## check code coverage quickly with the default Python
	coverage run --source $(MODULE) -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

.PHONY: docs
docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/$(MODULE).rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ $(MODULE)
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

.PHONY: servedocs
servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

.PHONY: release
release: dist ## package and upload a release
	python -m twine upload dist/*

.PHONY: check-release
check-release: dist ## check the release for errors
	python -m twine check dist/*

.PHONY: dist
dist: clean ## builds source and wheel package
	python -m build
	ls -l dist

.PHONY: install
install: uninstall ## install the package to the active Python's site-packages
	pip install .

.PHONY: uninstall
uninstall: clean ## uninstall the package
	pip uninstall --yes $(MODULE)
