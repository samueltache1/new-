import os
import json

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')

IDEAL_PH_RANGE = (6.0, 7.0)
OM_THRESHOLDS = {'low': 3.0, 'high': 6.0}


def _load_yaml(path):
    data = {}
    try:
        import yaml  # type: ignore
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
    except Exception:
        # Fallback: minimal YAML via json when subset is simple
        try:
            import re
            with open(path, 'r') as f:
                content = f.read()
            content = content.replace(': [', ': [').replace('{', '{').replace('}', '}')
            data = json.loads(json.dumps(eval("{" + content.replace('\n', ',') + "}")))
        except Exception:
            pass
    return data


def load():
    global IDEAL_PH_RANGE, OM_THRESHOLDS
    cfg = _load_yaml(CONFIG_PATH)
    if 'ideal_ph' in cfg:
        IDEAL_PH_RANGE = tuple(cfg['ideal_ph'])
    if 'om_thresholds' in cfg:
        OM_THRESHOLDS = cfg['om_thresholds']


# load configuration on module import
load()
