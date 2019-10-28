'''
Benutzer gibt Zahlen ein bis er 0 eingibt
Dann die höchste Zahl retournieren

Version1:
max_value = input('Wert eingeben?')
while int(max_value) != 0:
    user_input = input('Wert eingeben?')
    if int(max_value) < int(user_input):
        max_value = user_input
    elif int(user_input) == 0:
        break
print('max Wert:' + str(max_value))

Version2:
max_value = float('-inf')
user_input = 1
while int(user_input) != 0:
    user_input = input('Wert eingeben?')
    max_value = max( int(user_input), max_value)
print('max Wert:' + str(max_value))
Version3
'''
max = None
user_input = 1

while user_input!= 0.
    user_input = int(input('Zahl: '))
    if max is None or user_input > max:
        max = user_input
        
print("Höchste Zahl: " + max)