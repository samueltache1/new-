"""Simple soil analysis using configuration thresholds."""

from .config import IDEAL_PH_RANGE, OM_THRESHOLDS


def classify_ph(pH: float) -> str:
    if pH < IDEAL_PH_RANGE[0]:
        return 'acidic'
    if pH > IDEAL_PH_RANGE[1]:
        return 'alkaline'
    return 'optimal'


def analyze_soil(sample):
    report = {}
    ph_class = classify_ph(sample['pH'])
    report['pH'] = f"{sample['pH']} ({ph_class})"
    om = sample['organic_matter']
    if om < OM_THRESHOLDS['low']:
        om_desc = 'low'
    elif om > OM_THRESHOLDS['high']:
        om_desc = 'high'
    else:
        om_desc = 'moderate'
    report['organic_matter'] = f"{om}% ({om_desc})"
    report['moisture'] = f"{sample['moisture']}%"
    report['texture'] = (
        f"sand {sample['sand']}%, silt {sample['silt']}%, clay {sample['clay']}%"
    )
    return report
