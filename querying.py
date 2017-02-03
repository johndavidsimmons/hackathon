import sqlite3
conn = sqlite3.connect(r"C:\Users\nhounshell\Documents\github\hackathon\data-dev.sqlite")

c = conn.cursor()

def audience(choiceID, str=''):
    queries = {0: "select distinct Name from floorData where DisplayName like ?"
              ,1: 'select distinct Name from skill_mapping where skill like ?'
              ,2: 'select distinct Name from interest_mapping where interest like ?'
              ,3: 'select distinct Name from team_breakout where team == "BI IQ"'
              }
    if choiceID < 3:
        c.execute(queries[choiceID], ["%"+str+"%"])
    else:
        c.execute(queries[3])

    return [x[0] for x in c.fetchall()]