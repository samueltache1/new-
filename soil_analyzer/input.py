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
