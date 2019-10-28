'''
einlesen von CSV File


with open("daten.csv", "r") as file:
	lines = file.readlines()
	
print(lines)

am ende von with wird die Datei zugemacht
sobald das Python Programm geschloßen ist wird die Datei auch geschloßen

'''

import csv
from pprint import pprint 

with open("daten.csv", "r") as file:
    data= csv.reader(file, delimiter=',')
    #wenn ich aus dem with block draußen bin dann ist das file geschloßen
    pprint(list(data))
    

with open("daten.csv", "r") as file:
    lines = csv.reader(file, delimiter=',')
    #wenn ich aus dem with block draußen bin dann sind die daten in der liste gespeichert
    data = list(lines)

pprint(data)
    
with open("daten.csv", "r") as file:
    lines = csv.reader(file, delimiter=',')
    #zuerst zeile für zeile der daten bearbeiten und nicht das ganze file einlesen
    for line in lines:
        print(line)

