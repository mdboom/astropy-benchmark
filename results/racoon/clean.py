import os
import json

for file in os.listdir('.'):
    if file.endswith('.json'):
        d = json.load(open(file, 'rb'))
        if 'version' not in d:
            print(file)
            os.remove(file)
