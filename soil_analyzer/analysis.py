
        return 'alkaline'
    return 'optimal'



def analyze_soil(sample):
    report = {}
    ph_class = classify_ph(sample['pH'])
    report['pH'] = f"{sample['pH']} ({ph_class})"
    om = sample['organic_matter']

    return report
