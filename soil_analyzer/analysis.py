"""Simple soil analysis."""

from .config import IDEAL_PH_RANGE, OM_THRESHOLDS


def classify_ph(pH: float) -> str:
    if pH < IDEAL_PH_RANGE[0]:
        return 'acidic'
    if pH > IDEAL_PH_RANGE[1]:
        return 'alkaline'
    return 'optimal'


def classify_om(value: float) -> str:
    """Classify organic matter percentage."""
    if value < OM_THRESHOLDS['low']:
        return 'low'
    if value > OM_THRESHOLDS['high']:
        return 'high'
    return 'moderate'


def analyze_soil(sample):
    report = {}
    ph_class = classify_ph(sample['pH'])
    report['pH'] = f"{sample['pH']} ({ph_class})"
    om = sample['organic_matter']
    om_desc = classify_om(om)
    report['organic_matter'] = f"{om}% ({om_desc})"
    report['moisture'] = f"{sample['moisture']}%"
    report['texture'] = f"sand {sample['sand']}%, silt {sample['silt']}%, clay {sample['clay']}%"
    return report
