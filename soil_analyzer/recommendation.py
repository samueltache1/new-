"""Generate soil management recommendations."""

CROP_DATA = {
    'potato': (5.0, 6.5),
    'kale': (6.0, 7.5),
    'blueberry': (4.5, 5.5),
}


def recommend_amendments(sample):
    recs = []
    if sample['pH'] < 5.5:
        recs.append('apply lime or wood ash to raise pH')
    if sample['organic_matter'] < 3:
        recs.append('add compost or manure to increase organic matter')
    return recs


def recommend_crops(sample):
    ph = sample['pH']
    crops = [c for c, (lo, hi) in CROP_DATA.items() if lo <= ph <= hi]
    return crops
