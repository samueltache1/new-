"""Generate soil management recommendations.

Crop suitability and amendment rules are loaded from external data files so
that they can be updated without modifying the code. ``data/crops.csv`` defines
the preferred pH range for each crop and ``rules/amendments.yaml`` contains
simple amendment recommendations expressed as boolean conditions.
"""

from pathlib import Path
import csv

try:  # optional dependencies
    import pandas as pd
except Exception:  # pragma: no cover - pandas not always available
    pd = None

try:
    import yaml
except Exception:  # pragma: no cover - PyYAML may be missing
    yaml = None

try:
    import numexpr
except Exception:  # pragma: no cover - fallback if numexpr missing
    class _DummyNumexpr:
        @staticmethod
        def evaluate(expr, local_dict=None):
            return eval(expr, {}, local_dict or {})

    numexpr = _DummyNumexpr()


BASE_DIR = Path(__file__).resolve().parent.parent


def _load_crops():
    path = BASE_DIR / "data" / "crops.csv"
    if pd:
        df = pd.read_csv(path)
        return df.to_dict(orient="records")
    # simple CSV fallback
    with open(path, newline="") as fh:
        reader = csv.DictReader(fh)
        rows = []
        for row in reader:
            row["pH_min"] = float(row["pH_min"])
            row["pH_max"] = float(row["pH_max"])
            rows.append(row)
        return rows


def _load_rules():
    path = BASE_DIR / "rules" / "amendments.yaml"
    if yaml:
        with open(path, "r") as fh:
            data = yaml.safe_load(fh) or []
        return data
    # very small YAML subset parser
    rules = []
    current = None
    with open(path, "r") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            if line.startswith("-"):
                if current:
                    rules.append(current)
                current = {}
                line = line[1:].strip()
                if line:
                    k, v = line.split(":", 1)
                    current[k.strip()] = v.strip().strip("'\"")
            else:
                if ":" in line:
                    k, v = line.split(":", 1)
                    current[k.strip()] = v.strip().strip("'\"")
    if current:
        rules.append(current)
    return rules


_CROPS = _load_crops()
_RULES = _load_rules()


def recommend_amendments(sample):
    """Return a list of amendment suggestions for the given sample."""
    recs = []
    for rule in _RULES:
        cond = rule.get("condition")
        msg = rule.get("message", "")
        if not cond:
            continue
        try:
            if bool(numexpr.evaluate(cond, local_dict={"sample": sample})):
                recs.append(msg)
        except Exception:
            # if evaluation fails, skip the rule
            continue
    return recs


def recommend_crops(sample):
    """Return crop names suitable for the sample's pH."""
    ph = sample["pH"]
    crops = []
    for row in _CROPS:
        try:
            if float(row["pH_min"]) <= ph <= float(row["pH_max"]):
                crops.append(row["name"])
        except KeyError:
            continue
    return crops
