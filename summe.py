'''
beliebige Anzahl Zahlen vom User einlesen (bis 0)
in eine Liste geben

am ende alle Zahle der Liste summieren 
Summe und Liste ausgeben
github.com/MarkHofstetter/20191018-wifi-python

'''
liste = []
print(liste)
print('Zahlen eingeben: ')
print('Mit 0 beenden')
while True:
    user_input = input('Zahl: ')
    if user_input == '0':
        break
    try: 
        liste.append(int(user_input.strip()))
    except ValueError:
        print('Nummerischen Wert eingeben')
    except Error:
        print('Nummerischen Wert eingeben')    
summe = 0
print(liste)
for eintrag in liste:
    summe += eintrag
print('Summe der eingegebenen Werte ist: {0:d}'.format(summe))

