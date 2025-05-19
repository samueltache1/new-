import csv
import click

FIELDS = [
    'pH', 'moisture', 'organic_matter', 'sand', 'silt', 'clay'
]


def read_csv(path: str) -> list:
    """Read soil samples from CSV and return list of dicts."""
    samples = []
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            sample = {}
            for field in FIELDS:
                if field in row:
                    try:
                        sample[field] = float(row[field])
                    except (TypeError, ValueError):
                        sample[field] = None
                else:
                    sample[field] = None
            # warn if texture percentages don't sum to roughly 100
            sand = sample.get('sand') or 0
            silt = sample.get('silt') or 0
            clay = sample.get('clay') or 0
            total = sand + silt + clay
            if abs(total - 100) > 5:
                click.echo(
                    f"Warning: texture percentages total {total:.1f} (expected ~100)",
                    err=True,
                )
            samples.append(sample)
    return samples
