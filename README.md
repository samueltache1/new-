# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and get basic recommendations. It is an early prototype inspired by the larger
blueprint described in the repository issues.

Crop information and amendment rules are stored in ``data/crops.csv`` and
``rules/amendments.yaml`` so new guidance can be added without code changes.

## Usage

Run interactively:

```bash
python -m soil_analyzer.cli --interactive
```

The recommendation engine loads crop data from ``data/crops.csv`` and amendment
rules from ``rules/amendments.yaml``. If `pandas` and `PyYAML` are installed
they will be used to parse these files, otherwise simple fallbacks handle the
parsing.

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```
