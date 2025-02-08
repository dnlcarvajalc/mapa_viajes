# Variables
VENV=.venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

# Default target
.PHONY: all
all: install lint format run

# Create and activate virtual environment
.PHONY: venv
venv:
	python3 -m venv $(VENV)
	echo "source $(VENV)/bin/activate" >> .venv/bin/activate_make

# Install dependencies
.PHONY: install
install: venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Run tests with pytest
.PHONY: test
test: install
	$(PYTHON) -m pytest tests/

# Linting with flake8
.PHONY: lint
lint: install
	$(PYTHON) -m flake8 --exit-zero src/

# Formatting with black
.PHONY: format
format: install
	$(PYTHON) -m black src/

# Clean up generated files
.PHONY: clean
clean:
	rm -rf $(VENV) .pytest_cache __pycache__ *.pyc *.pyo

# Execute the main script
.PHONY: run
run: install
	$(PYTHON) src/main.py