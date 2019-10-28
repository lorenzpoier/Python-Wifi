wort= 'irgendwas'
laenge = len(wort)

print('Das Wort {:s} ist {:d} Zeichen lang'.format(wort, laenge))

wort1 = 'nochwas'
print('{:s} {:s}'.format(wort, wort1))
satz = '{:s} {:s}'.format(wort, wort1)
print(satz)
print('=' * 10)
print('=' * len(satz))

print(wort.upper())
print('HALLO'.lower())

#Variable Wort bleibt unverändert
print(wort.replace('was', 'wie'))


if 'was' in wort:
    print('was ist enthalten')
