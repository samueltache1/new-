import csv

        reader = csv.DictReader(f)
        for row in reader:
            sample = {}
            for field in FIELDS:

            samples.append(sample)
    return samples
