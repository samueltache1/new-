"""Load configuration from YAML file."""
import os
from ast import literal_eval

# Path to config.yaml in repo root
_CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config.yaml')


def _parse_value(value: str):
    value = value.strip()
    if value.startswith('[') and value.endswith(']'):
        return [float(v.strip()) for v in value[1:-1].split(',') if v.strip()]
    if value.startswith('{') and value.endswith('}'):
        obj = {}
        items = [item for item in value[1:-1].split(',') if item.strip()]
        for item in items:
            k, v = item.split(':')
            obj[k.strip()] = float(v)
        return obj
    try:
        return literal_eval(value)
    except Exception:
        return value


def _load_config(path: str):
    data = {}
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            key, val = line.split(':', 1)
            data[key.strip()] = _parse_value(val)
    return data

_CONFIG = _load_config(_CONFIG_PATH)

IDEAL_PH_RANGE = tuple(_CONFIG.get('ideal_ph', [6.0, 7.0]))
OM_THRESHOLDS = _CONFIG.get('om_thresholds', {'low': 3.0, 'high': 6.0})
