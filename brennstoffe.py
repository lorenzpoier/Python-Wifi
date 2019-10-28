'''
+ Ausgabe des Brennstoffnamens
+ erste Jahr mit dem höchsten Preis und dem Durchschnittspreis

A: 567 380
B: 12   10

+ Grafik des Preisverlaufs

'''
import csv
from pprint import pprint 
from matplotlib import pyplot as plt
print('############################ 1.Versuch mit Schleife im with Block ###################')     
   
with open("daten.csv", "r") as file:
    lines = csv.reader(file, delimiter=',')
    first_line = True
    #zuerst zeile für zeile der daten bearbeiten und nicht das ganze file einlesen
    for line in lines:
        if first_line == True:
            first_line = False
        else:
            liste = list(line[1:])
            liste = [float(i) for i in liste]
            Durchschnittspreis = sum(liste)/len(liste)
            maxPreis = max(liste)
            print(line[0], ': Durchschnittspreis = {:0.2f}, Maximal Preis = {:0.2f}'.format(Durchschnittspreis, maxPreis))
            
print('############################ 2.Versuch mit exportierter Liste ###################')        
with open("daten.csv", "r") as file:
    lines = csv.reader(file, delimiter=',')
    data = list(lines)
    
    #zuerst zeile für zeile der daten bearbeiten und nicht das ganze file einlesen
fig, ax = plt.subplots(int(len(data[0])/2)-1,2)
item1 = -1
item2 = 0
for line in data[1:]:
    liste = [float(i) for i in line[1:]]
    if item1 <5:
        item1 += 1
    elif item1==5:
        item1 = 0
        item2 = 1
    ax[item1,item2].plot(data[0][1:], liste )
    ax[item1,item2].set_title(line[0])
    ax[item1,item2].set_xlabel('Jahr')
    ax[item1,item2].set_ylabel('Preis')
    
    Durchschnittspreis = sum(liste)/len(liste)
    maxPreis = max(liste)
    JahrmitmaxPreis = liste.index(max(liste))
    print(line[0], ': Durchschnittspreis = {:0.2f}, Maximal Preis = {:0.2f} im Jahr {:s}'.format(Durchschnittspreis, maxPreis, data[0][JahrmitmaxPreis+1]))
plt.savefig('Brennstoffe.png')  
#plt.show()

print('############################ 3.Versuch mit exportierter Liste ###################')        
with open("daten.csv", "r") as file:
    lines = csv.reader(file, delimiter=',')
    data = list(lines)
    
    #zuerst zeile für zeile der daten bearbeiten und nicht das ganze file einlesen

for line in data[1:]:
    liste = [float(i) for i in line[1:]]
    fig, ax = plt.subplots()
    ax.plot(data[0][1:], liste )
    ax.set_title(line[0])
    ax.set_xlabel('Jahr')
    ax.set_ylabel('Preis')
    plt.show()
    Durchschnittspreis = sum(liste)/len(liste)
    maxPreis = max(liste)
    JahrmitmaxPreis = liste.index(max(liste))
    print(line[0], ': Durchschnittspreis = {:0.2f}, Maximal Preis = {:0.2f} im Jahr {:s}'.format(Durchschnittspreis, maxPreis, data[0][JahrmitmaxPreis+1]))
   
