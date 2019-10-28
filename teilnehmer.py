
'''
Array mit liste aller Teilnehmer

'''

teilnehmer = [ 
    'Lydia',
    'Magdalena',
    'Herbert',
    'Tobias',
    'Clemens',
    'Sarah',
    'Elias',
    'Zsolt',
    'Birgit',
    'Lorenz',
    'Mark',
    ]
# Dies ändert die Liste    
teilnehmer.sort()
for (i, tn) in enumerate(teilnehmer):
    print('{0:-05d} {1:s}'.format(i, tn))

user_input = input('bitte gewünschten Teilnehmer suchen?')    
if user_input.strip() in teilnehmer:
    print('{:s} ist da'.format(user_input))
else:
    print('{:s} ist nicht da'.format(user_input))
    