import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

paths = []

def path_join(prefix, suffix:str):
    if suffix.startswith('='):
        return prefix + suffix 
    else:
        return prefix + '/' + suffix

def flatten(payload):
    if isinstance(payload, dict):
        result = []
        for key, value in payload.items():
            result += [path_join(key, item) for item in flatten(value)]
        return result
    elif isinstance(payload, list):
        result = []
        for idx, value in enumerate(payload):
            result += [path_join(f'[{idx}]', item) for item in flatten(value)]
        return result
    else:
        return ['=' + str(payload)]

def read_json_as_flat(filepath):
    try:
        with open(filepath) as f:
            content = flatten(json.load(f))
    except Exception as e:
        content = {f'error reading {filepath}': str(e)}    
    return content

if len(sys.argv) > 1:
    from glob import glob
    for arg in sys.argv[1:]:
        paths += glob(arg)
        if arg == '|':
            break
else:
    print('Usage: readpl -i [pattern to match jsons] [pattern to match xpath]')
    exit(0)

jsonFiles = [f for f in paths if str(f).endswith('.json')]

if not jsonFiles:
    print('No json files found with patterns: ' + ' '.join(sys.argv[1:]))
    exit(0)

for jsonFilePath in jsonFiles:
    flatjson = read_json_as_flat(jsonFilePath)
    for line in flatjson:
        try:
            print(jsonFilePath + ': ' + line)
        except BrokenPipeError:
            exit(0)