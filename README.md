# Intelligent Soil Condition Analyzer

This project provides a minimal command line tool to analyze soil parameters
and get basic recommendations. It is an early prototype inspired by the larger
blueprint described in the repository issues.

## Usage

Run interactively:

```bash
python -m soil_analyzer.cli --interactive
```

To analyze samples from a CSV file, use the helper `read_csv`:

```python
from soil_analyzer.io import read_csv
samples = read_csv("samples.csv")
```

This loader converts numeric fields and issues a warning if sand, silt and
clay percentages do not sum to roughly 100%.

## Tests

Execute unit tests with:

```bash
python -m unittest discover -s soil_analyzer/tests
```
