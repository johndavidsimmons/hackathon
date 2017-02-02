import json
import pandas as pd

data = json.loads(open("C:\Temp\wewlad.json").read())

skills = []
interests = []
for tm in data['results']:
    try:
        name = tm['firstName'] + ' ' + tm['lastName']
        for skill in tm['skills']:
            skills.append((name, skill.lower()))
        for interest in tm['interests']:
            interests.append((name, interest.lower()))
    except:
        pass