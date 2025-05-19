# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and get basic recommendations. It is an early prototype inspired by the larger
blueprint described in the repository issues.

## Usage

The application loads thresholds from `config.yaml` in the project root.

Run interactively:

```bash
python -m soil_analyzer.cli --interactive
```

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```

## Configuration

`config.yaml` defines the ideal pH range and organic matter thresholds.
Modify these values to adjust soil classification boundaries without
changing the code.
