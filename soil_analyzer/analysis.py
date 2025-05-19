
        return 'alkaline'
    return 'optimal'


def analyze_soil(sample):
    report = {}
    ph_class = classify_ph(sample['pH'])
    report['pH'] = f"{sample['pH']} ({ph_class})"
    om = sample['organic_matter']

        om_desc = 'high'
    else:
        om_desc = 'moderate'
    report['organic_matter'] = f"{om}% ({om_desc})"
    report['moisture'] = f"{sample['moisture']}%"

    return report
