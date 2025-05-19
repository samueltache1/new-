# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and return simple recommendations. The CLI is built with [Click](https://click.palletsprojects.com/) and can run interactively or on a CSV file.

Package metadata is defined in `pyproject.toml` targeting Python 3.10+ and
listing the main dependencies.

## Usage

Run interactively:

```bash
python -m soil_analyzer.cli analyze --interactive
```

Analyze a CSV file:

```bash
python -m soil_analyzer.cli analyze-csv samples.csv
```

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```
