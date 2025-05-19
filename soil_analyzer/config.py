import os

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')


def _simple_yaml_parse(text: str) -> dict:
    result = {}
    current_key = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith('#'):
            continue
        if line.startswith(' '):
            if current_key:
                sub_key, val = line.strip().split(':', 1)
                result.setdefault(current_key, {})[sub_key.strip()] = float(val.strip())
            continue
        if ':' in line:
            key, val = line.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val.startswith('[') and val.endswith(']'):
                vals = [float(v.strip()) for v in val.strip('[]').split(',') if v.strip()]
                result[key] = vals
                current_key = None
            elif val == '':
                result[key] = {}
                current_key = key
            else:
                try:
                    result[key] = float(val)
                except ValueError:
                    result[key] = val
                current_key = None
    return result


def load_config(path: str = CONFIG_PATH) -> dict:
    try:
        import yaml  # type: ignore
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception:
        with open(path, 'r', encoding='utf-8') as f:
            return _simple_yaml_parse(f.read())


_config = load_config()
IDEAL_PH_RANGE = tuple(_config.get('ideal_ph', [6.0, 7.0]))
OM_THRESHOLDS = _config.get('om_thresholds', {'low': 3.0, 'high': 6.0})
