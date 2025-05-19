"""Data input helpers."""

def prompt_for_soil_data():
    """Prompt user for soil data and return a sample dict."""
    sample = {}
    sample['pH'] = float(input('Enter soil pH: '))
    sample['moisture'] = float(input('Enter soil moisture (%): '))
    sample['organic_matter'] = float(input('Enter organic matter (%): '))
    texture = input("Enter sand,silt,clay percentages (comma separated): ")
    sand, silt, clay = [float(v) for v in texture.split(',')]
    sample['sand'] = sand
    sample['silt'] = silt
    sample['clay'] = clay
    return sample


def read_soil_data_from_csv(path):
    """Load soil samples from a CSV file.

    Each row should provide the columns pH, moisture, organic_matter,
    sand, silt and clay. Additional columns are ignored.
    """
    import csv

    samples = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                sample = {
                    "pH": float(row["pH"]),
                    "moisture": float(row["moisture"]),
                    "organic_matter": float(row["organic_matter"]),
                    "sand": float(row["sand"]),
                    "silt": float(row["silt"]),
                    "clay": float(row["clay"]),
                }
            except KeyError as exc:
                raise ValueError(f"Missing required column: {exc}") from exc
            samples.append(sample)
    return samples
