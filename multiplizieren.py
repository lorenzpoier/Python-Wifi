'''
Programm: Kopfrechnen
Benutzer bekommt 2 unterschiedliche Zufallszahlen: 1-10
Benutzer multipliziert

10 verschiedene Aufgaben stellen und Richtung und falsch Auswerten


import random
korrekt = 0
# \n fügt eine neue Zeile ein
Anzahl_Aufgaben = input('Wie viele Beispiele sollen gerechnet werden?')
Anzahl_Aufgaben = int(Anzahl_Aufgaben)
for i in range(Anzahl_Aufgaben):
    while True:
        random_value_1 = random.randint(1,10)
        random_value_2 = random.randint(1,10)
        if random_value_1 != random_value_2:
            break
    print('Muliplikation von ', str(random_value_1), '*',  str(random_value_2))
    user_input = input('Bitte das Ergebnis der Mulitplikation eingeben: ')
    multiplikation_ergebnis =  random_value_1 * random_value_2
    if int(user_input) == multiplikation_ergebnis:
        korrekt += 1 
print('Korrekte Ergebnisse:' + str(korrekt))
print('Falsche Ergebnisse:' + str(Anzahl_Aufgaben - korrekt))
print(i+1)
'''
import random
right = 0
# \n fügt eine neue Zeile ein
while True:
    try:
        nr_exercises = input('Wie viele Beispiele sollen gerechnet werden?')
        nr_exercises = int(nr_exercises)
        if nr_exercises <= 0:
            print('Zahl muss größer als 0 sein!')
            continue
        break
    except ValueError:
        print('ungültiger Wert')
    except Error:
        print('es ist was anderes passiert!')

        

for i in range(nr_exercises):
    random_value_1 = random.randint(1,10)
    random_value_2 = random.randint(1,10)
    print('Muliplikation von ', str(random_value_1), '*',  str(random_value_2))
    user_input = input('Bitte das Ergebnis der Mulitplikation eingeben: ')
    product =  random_value_1 * random_value_2
    if int(user_input) == product:
        right += 1 
print('Korrekte Ergebnisse:' + str(right))
print('Falsche Ergebnisse:' + str(nr_exercises - right))
# Buch 150
print('Korrekt  {:0.2f} %'.format(right/(i+1)*100))