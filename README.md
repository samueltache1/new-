# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and get basic recommendations. It is an early prototype inspired by the larger
blueprint described in the repository issues.

## Usage

Run interactively:

```bash
python -m soil_analyzer.cli --interactive
```

### Configuration

Thresholds for pH and organic matter are stored in `config.yaml` at the
repository root. Modify this file to adjust ideal pH or organic matter ranges
without changing the code.

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```
