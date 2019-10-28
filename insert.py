'''
SQLite DB
Datensätze einfügen
zum erstellen der DB im command : sqlite3 students.db
zum erstellen der tabelle im command: CREATE TABLE student (
id INTEGER NOT NULL,
name VARCHAR(50) NOT NULL,
birth_year VARCHAR(50) NOT NULL,
PRIMARY KEY (id)
);
'''

import sqlite3
conn = sqlite3.connect('students.db')

teilnehmer = { 
    'Lydia': {'yob':1981, 'fav_col': 'grün', 'edu': ['VS', 'Gym', 'Uni']},
    'Magdalena': {'yob':1982},
    'Herbert': {'yob':1973},
    'Tobias': {'yob':1984},
    'Clemens': {'yob':1989},
    'Sarah': {'yob':1994, 'fav_col': 'lila'},
    'Elias': {'yob':1997},
    'Zsolt': {'yob':1988},
    'Birgit': {'yob':1987},
    'Lorenz': {'yob': 1987, 'edu':['VS', 'HAK', 'wifi']},
    'Mark': {'yob': 1975, 'fav_col': 'blau', 'edu':['VS', 'Gym', 'Uni']},
    }

for name, gebjahr in teilnehmer.items():
    conn.execute("insert into student(name, birth_year) values (?,?)",(name, gebjahr['yob']))

'''
teilnehmer = {
'Martin': 1976,
'Harald': 1970,
'Gerald': 1973,
'RolandW': 1998,
'Christoph': 1981,
'RolandS': 1974,
}

#for name, birth_year in teilnehmer.items():
#conn.execute("insert into student(name, birth_year) values (?,?)",
#(name, birth_year))
'''
conn.commit()
