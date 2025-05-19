"""Simple soil analysis."""

from . import config


def classify_ph(pH: float) -> str:
    """Classify pH using thresholds from configuration."""
    low, high = config.IDEAL_PH_RANGE
    if pH < low:
        return 'acidic'
    if pH > high:
        return 'alkaline'
    return 'optimal'


def analyze_soil(sample):
    report = {}
    ph_class = classify_ph(sample['pH'])
    report['pH'] = f"{sample['pH']} ({ph_class})"
    om = sample['organic_matter']
    if om < config.OM_THRESHOLDS['low']:
        om_desc = 'low'
    elif om > config.OM_THRESHOLDS['high']:
        om_desc = 'high'
    else:
        om_desc = 'moderate'
    report['organic_matter'] = f"{om}% ({om_desc})"
    report['moisture'] = f"{sample['moisture']}%"
    report['texture'] = f"sand {sample['sand']}%, silt {sample['silt']}%, clay {sample['clay']}%"
    return report
