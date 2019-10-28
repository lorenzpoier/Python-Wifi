'''
Error Handling
try catch



a = 10
b = input('Divisor: ')
try:
    b = int(b)
except ValueError:
    print('ungültiger Wert')
    exit

try:
    print(a/b)
#except Error
#except Error fängt jeden Fehler ab
except ZeroDivisionError:
    print('Division durch 0!')
    '''
a = 10
b = input('Divisor: ')

try:
    b = int(b)
    print(a/b)
except ValueError:
    print('ungültiger Wert')
#except Error
#except Error fängt jeden Fehler ab
except ZeroDivisionError:
    print('Division durch 0!')
except Error:
    print('es ist was anderes passier!')
    
