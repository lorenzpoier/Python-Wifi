'''

Tuple 

List die unveränderlich ist

Dictionary
{}

'''
from pprint import pprint

#benanntes übergeben von parameter und default festlegung 
def user_input_name(question = 'Namen eingeben: '):
    try:
        user_input = input(question)
        test = teilnehmer[user_input]
        return user_input        
    except NameError:
        #user_input = "ungültige Eingabe, Teilnehmer nicht angemeldet"
        user_input = "Exit"
        return user_input
    except KeyError:
        #user_input = "ungültige Eingabe, Teilnehmer nicht angemeldet"
        user_input = "Exit"
        return user_input
    except Error:
        #user_input = "ungültige Eingabe, Teilnehmer nicht angemeldet"
        user_input = "Exit"
        return user_input
    
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
'''
print('Abbruch mit Exit')
while True:
    user_input = user_input_name('Teilnehmer suchen: ')
    if user_input == "Exit":
        break
    elif user_input ==  "ungültige Eingabe, Teilnehmer nicht angemeldet":
        print("ungültige Eingabe, Teilnehmer nicht angemeldet")
    else:
        print(user_input)

teilnehmer['Eva'] = 1980

geburtsdaten = list(teilnehmer.values())
#Die gesamte Liste wird sortiert
geburtsdaten.sort() 
print(geburtsdaten)
'''
pprint(teilnehmer) 
user_input = user_input_name('Teilnehmer suchen: ')
if user_input == "Exit":
    print("ungültige Eingabe, Teilnehmer nicht angemeldet")
else:
    print('{:s} geboren in {:d}'.format(user_input, teilnehmer[user_input]['yob']))
    try:
        print('{:s} Lieblingsfarbe ist {:s}'.format(user_input, teilnehmer[user_input]['fav_col']))
    except:
        print('{:s} hat keine Lieblingsfarbe'.format(user_input))
#dem gewählten Teilnehmer eine Ausbildung hinzufügen'
    edu_zusatz = input('Neue Ausbildung eingeben: ')
    if 'edu' in teilnehmer[user_input]:            
            teilnehmer[user_input]['edu'].append(edu_zusatz)
    else:
        teilnehmer[user_input]['edu'] = [edu_zusatz]
    try:
        print('{:s} höchste abgeschlossene Ausbildung ist {:s}'.format(user_input, teilnehmer[user_input]['edu'][-1]))
    except:
        print('{:s} hatte keine Ausbildungsinformation gespeichert.'.format(user_input))
'''
    if 'edu' in teilnehmer[user_input]:
        print()
    else:
        print('{:s} hat keine Ausbildungsinformation gespeichert.'.format(user_input))
'''



