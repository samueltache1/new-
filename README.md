# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and get basic recommendations. It is an early prototype inspired by the larger
blueprint described in the repository issues.

## Usage

Run interactively:

```bash
python -m soil_analyzer.cli --interactive
```

The CLI prints a formatted report using `format_report` from
`soil_analyzer.formatting`. Section titles appear in bold when your terminal
supports ANSI escape sequences.

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```
