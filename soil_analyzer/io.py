import csv
from typing import List, Dict

FIELDS = ["pH", "moisture", "organic_matter", "sand", "silt", "clay"]


def read_csv(path: str) -> List[Dict[str, float]]:
    """Read soil samples from CSV file and return a list of dictionaries.

    Extra columns are ignored. Required numeric fields are converted to float.
    """
    samples: List[Dict[str, float]] = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sample = {}
            for field in FIELDS:
                value = row.get(field)
                if value is None:
                    raise KeyError(f"Missing column '{field}' in CSV")
                sample[field] = float(value)
            samples.append(sample)
    return samples
