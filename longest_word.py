'''
Benutzer gibt Wörter ein bis er 0 eingibt
Dann das längste Wort mit der Zahl der Buchstaben retournieren

Version1:
'''
max = None
user_input = '1'
while user_input != str(0):
    user_input = input('Wort: ')
    if max is None or len(user_input) > max:
        max_wort = user_input
        max = len(user_input)
print('Das längste Wort {:s} ist {:d} Zeichen lang'.format(max_wort, max))