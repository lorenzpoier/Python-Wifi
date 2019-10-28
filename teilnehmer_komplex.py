
'''
Array mit liste aller Teilnehmer
und Geburtsjahr

'''
from pprint import pprint

teilnehmer = [ 
    ['Lydia',1981, 'grün'],
    ['Magdalena',1982],
    ['Herbert',1973],
    ['Tobias',1984],
    ['Clemens',1989],
    ['Sarah',1994],
    ['Elias',1997],
    ['Zsolt',1988],
    ['Birgit',1987],
    ['Lorenz',1987],
    ['Mark',1975, 'blau', ['VS', 'Gym', 'Uni']],
    ]

'''

Wir lesen eine usereingabe (name) und durchsuchen die liste nach dem geburtsjahr oder fehlermeldung 

teilnehmer[0].append('rot')
teilnehmer[0].append('VS')
teilnehmer[0][-1].append('NMS')

#Pretty Print
#pprint(teilnehmer)
# Dies ändert die Liste   
#teilnehmer.sort()
user_input_namen_suche = input('Teilnehmer suchen?')

gefunden = 0
for (i, tn) in enumerate(teilnehmer):
    if tn[0] == user_input_namen_suche:
        if len(tn) == 3:
            print('{0:-05d} {1:s} geboren {2:d} mit Lieblingsfarbe {3:s}'.format(i, tn[0], tn[1], tn[2]))
        else:
            print('{0:-05d} {1:s} geboren {2:d}'.format(i, tn[0], tn[1]))
        gefunden = 1

#print('ende schleife: {0:s} \n länge teilnehmer liste: {1:d}'.format(str(i), len(teilnehmer)))

if gefunden == 0:
    print('{:s} nicht vorhanden in der Teilnehmerliste'.format(user_input_namen_suche))
'''
user_input_namen_suche = input('Teilnehmer suchen?')
user_input_namen_suche_lower = user_input_namen_suche.lower().strip()
gefunden = False
for (i, tn) in enumerate(teilnehmer):
    tn_name_lower = tn[0].lower()
    if tn_name_lower == user_input_namen_suche_lower:
        try:
            print('{0:-05d} {1:s} geboren {2:d} mit Lieblingsfarbe {3:s}'.format(i, tn[0], tn[1], tn[2]))
        except IndexError:
            print('{0:-05d} {1:s} geboren {2:d}'.format(i, tn[0], tn[1]))
        gefunden = True
        try:
        #format kann keine Liste retournieren
            print('Höchster Bildungsabschluss {0:s}'.format(tn[3][-1]))
        except IndexError:
            print('Keine Bildungsdaten vorhanden')
#try:
#   print(tn[2])
#except IndexError:
#   pass
#pass Platzhalter falls was stehen muss , verhindert Fehlermeldungen


#print('ende schleife: {0:s} \n länge teilnehmer liste: {1:d}'.format(str(i), len(teilnehmer)))

#if gefunden is false:
if not gefunden:
    print('{:s} nicht vorhanden in der Teilnehmerliste'.format(user_input_namen_suche))

