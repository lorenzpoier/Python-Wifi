'''
eng2ger 



eng2ger = {
    'dog': 'hund',
    'cat': 'katze',
    }
# Retourübersetzung
# Array leer anlegen und die Variablen vertauschen
ger2eng = {}    
for k,v in eng2ger.items():
    ger2eng[v] = k
print(ger2eng)
#in einem Schritt , Schleife bleibt ident und dict((v,k) ...) bedeutet:
# erstelle ein Dictionary mit Key=v und Value = k
ger2eng = dict((v,k) for k,v in eng2ger.items())
ger2eng = dict( zip(eng2ger.values(), eng2ger.keys()) )
print('##############################')
print(ger2eng)


der user kann ein deutsches oder englisches wort einfügen
und bekommt die Übersetzung retour, bzw. Fehlermeldung

input_user = input('Deutsches oder Englisches Wort eingeben: ')
print(eng2ger.items())
if input_user in eng2ger.keys():
    uebersetzung = eng2ger[input_user]
elif input_user in ger2eng.keys():
    uebersetzung = ger2eng[input_user]
else:    
    uebersetzung = 'Keine passende Uebersetzung gefunden'

print(uebersetzung)

'''
import configparser
from pprint import pprint
'''
Syntax Fehler im Config File können besser gehandelt werden als im Programm File 
modul argparse dient für komplexere configfiles
'''
#Config Parser Objekt wird initialisiert
config = configparser.ConfigParser()
#spezfische Konfiguration wird ausgelesen
config.read('woerterbuch.ini')
#Konfiguration enthält Sections
config.sections()
how_many_words2translate = int(config['parameter']['how_many_words2translate'])
english_to_german = dict(config['english_to_german'])
german_to_english = dict((v,k) for k,v in english_to_german.items())
print(how_many_words2translate)
for i in range(how_many_words2translate):
    search = input('zu übersetzendes wort: ') 
    if search in english_to_german:
        print('Englisch: {:s} Deutsch: {:s}'.format(search, english_to_german[search]))
    elif search in german_to_english:
        print('Deutsch: {:s} Englisch: {:s}'.format(search, german_to_english[search]))
    else:
        print('nichts gefunden')
    