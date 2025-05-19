# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and get basic recommendations. It is an early prototype inspired by the larger
blueprint described in the repository issues.

## Usage

Run interactively:

```bash
python -m soil_analyzer.cli --interactive
```

## Packaging

The project is configured with a `pyproject.toml` for modern packaging.
Dependencies include `click`, `pandas`, `scikit-learn` and `PyYAML`.
Python 3.10 or newer is required.

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```
