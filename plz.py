import re

'''
eine österreichische pLZ beginnt mit einem A (groß oder klein)
dann darf ein - oder ein Leerzeichen oder nichts sein
dannach genau 4 Ziffern
üben von regexpressions im web: zb.: https://regexr.com/

+ davon darf die erste nicht 0 werden
+ beliebig viele whitespaces 
(welche Characterclass)

+10 Beispiele in ein dictionary
key = PLZ
value = True oder False
5 true und 5 false

+ Iteration über das Dictionary
+ regex drauf anwenden und ausgabe wenn der erwartungswert nicht 
mit dem Ergebnis übereinstimmt


strip
'''

PLZDictionary = {
'A-1234': True,
'A-0234': False,
'A 1234': True,
'A    9999': True,
'A 1234a': False,
'A 1 2 3 4': False,
'D 12345': False,
'A- - 1234': True,
'a-1234': True,
'1234': False,
}

for plz, value in PLZDictionary.items():
    print(plz, value)
    match = re.search(r'^[Aa][-\s]{0,}[1-9]\d{3}$', plz)
    #print(match)
    if  (match is None and value is True) or \
        (match and value is False):
        print('{0:s} falsch klassifiziert'.format(plz))
    else:
        print('korrekt klassifiziert'.format(plz))

'''
plz = 'A-1234'
#eine Menge wird in eckigen Klammer geschrieben
#^ String muss beginnen mit
#$ muss enden mit
#{} länge des strings
#[] muss enthalten
# Zeichen auflisten oder mit 0-9 als bis definieren
#\d  Digit - Zahlen kann auch [0-9] geschrieben werden
# * ist quantifikator dann kann das zeichen davor unendlich of vorkommen
#{0,} definiert auch die länge vom string mit 0-unendlich
#() es wird markiert was extrahiert werden soll

match = re.search(r'^[Aa][- ]{0,1}[1-9]\d{3}$', plz)
#\s{0-} retourniert Leerzeichen
#\S retourniert alles ausgenommen Leerzeichen

if match:
    print('ist eine österreichische PLZ')
else:
    print('ist keine österreichische PLZ')
'''
    