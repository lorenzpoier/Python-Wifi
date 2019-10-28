'''

Benutzer soll einen Suchstring eingeben
und als Antwort erhalten ob der string im Text enthalten ist
Gross/Kleinschreibung ignorieren

zusatz: leading und trailing spaces sollen ignoriert werden


text = 'Wir haben einen langen Text'
text = text.replace(" ", "")
user_input = input("Suchstring eingeben: ")
user_input = user_input.replace(" ", "")

if user_input.lower() in text.lower():
    print("Text {:s} ist enthalten!".format(user_input))
else:
    print("Text {:s} ist nicht enhalten!".format(user_input))
'''

text = 'Wir haben einen langen Text'
user_input = input("Suchstring eingeben: ")
#Strip entfernt trailing und leading spaces
if user_input.strip().lower() in text.lower():
    print("Text {:s} ist enthalten!".format(user_input))
else:
    print("Text {:s} ist nicht enhalten!".format(user_input))
