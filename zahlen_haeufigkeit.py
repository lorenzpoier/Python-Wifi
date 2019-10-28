'''

Zahlenhäufigkeit

User gibt Zahlen ein 
0 = Ende

am ende wird ausgegeben (einfach mit pprint) wie of eine Zahl eingegeben wurde
'''

from pprint import pprint

#benanntes übergeben von parameter und default festlegung 
def user_input_positive_number(question = 'Wert eingeben: '):
    while True:
        try:
            user_input = input(question)
            user_input = int(user_input)
            if user_input < 0:
                print("Zahl muß größer 0 sein")
                continue
            break
        except ValueError:
            print("ungültige Eingabe")
    return user_input



zahlendict = {
    0: {'Anzahl': 0},
    }
while True:
    user_input = user_input_positive_number('Zahl eingeben, mit 0 beenden:')
    if user_input == 0:
        break
    if user_input in zahlendict.keys():
        zahlendict[user_input]['Anzahl']+= 1
    else:
        zahlendict[user_input] = {'Anzahl': 1}
pprint(zahlendict)
     
'''
zahlendict = {}
while True:
    user_input = input('Zahl eingeben, mit 0 beenden:')
    if user_input == '0':
        break
    if user_input in zahlendict:
        zahlendict[user_input] += 1
    else:
        zahlendict[user_input] = 1
pprint(zahlendict)
'''



