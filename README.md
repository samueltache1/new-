# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and get basic recommendations. It is an early prototype inspired by the larger
blueprint described in the repository issues.

## Usage

Run interactively:

```bash
python -m soil_analyzer.cli interactive
```

Analyze a CSV file:

```bash
python -m soil_analyzer.cli analyze-csv samples.csv
```

Use `--help` on the main command or any subcommand to see a one-line
usage example in the help text.

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```
