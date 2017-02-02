import json
import pandas as pd

data = json.loads(open("C:\Temp\wewlad.json").read())

skills = []
interests = []
logins = []
for tm in data['results']:
    try:
        if tm['division'] != 'Business Intelligence': continue
        name = tm['firstName'] + ' ' + tm['lastName']
        for skill in tm['skills']:
            skills.append((name, skill.lower()))
        for interest in tm['interests']:
            interests.append((name, interest.lower()))
        logins.append((name, tm['email'], tm['extension']))
    except:
        pass