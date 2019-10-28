'''
zahlen raten:
zufallszahl zw 1-100
benutzer bekommt info ob zu hoch oder niedrig geraten wurde
5 mal maximal raten
binär teilen maximal 7 bei 128 werten
'''

import random

#benanntes übergeben von parameter und default festlegung 
def user_input_positive_number(question = 'Wert eingeben: '):
    while True:
        try:
            user_input = input(question)
            user_input = int(user_input)
            if user_input <= 0:
                print("Zahl muß größer 0 sein")
                continue
            break
        except ValueError:
            print("ungültige Eingabe")
    return user_input


random_value = random.randint(0,128)
user_input = user_input_positive_number('Bitte eine Zahl zwischen 0 und 128 eingeben: ')
anzahlversuche = 6
i = 0
print (i, anzahlversuche)
while i < anzahlversuche:
    if user_input < random_value:
        print('Random Wert höher als {:d}'.format(user_input))
    elif user_input > random_value:
        print('Random Wert niedriger als {:d}'.format(user_input))
    else:
        print('Random Wert ist {:d}'.format(user_input))
        break
    user_input = user_input_positive_number('Bitte eine Zahl zwischen 0 und 128 eingeben: ')
    i += 1
if user_input == random_value:    
     print('Random Value war {:d} und wurde nach {:d} Versuchen  erraten!'.format(random_value, i+1))
else:
    print('Random Value war {:d} und wurde nach {:d} Versuchen nicht erraten!'.format(random_value, anzahlversuche+1))

