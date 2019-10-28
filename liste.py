#Listen werden mit eckigen Klammern initialisiert
#Listen mit Beistrich beenden, ist möglich und gewünscht
#    0  1  2  3  4  5   6
f = [1, 1, 2, 3, 5, 8, 13,]

print(f)
print(f[3])
#letztes element
print(f[-1])
print(f[0:3])
#bis zum letzten element
print(f[3:])
#Elemente einer Liste könnnen unterschiedlichen Datentypen haben
#f[4] = 'Hallo'
print(f)

print(len(f))

print(f[3], f[5])
d = [f[3], f[5]]
print(d)

#hängt am ende der liste an
f.append(21)
#erste 0 ist die Position und dannach der Wert
f.insert(0,0)
print(f)
#geht auf Werte nicht Indices, entfernt das erste Vorkommen dieses Wertes in der Liste
f.remove(1)
#Listenfunktionen arbeiten direkt auf der Liste und retournieren nicht die geänderte Liste, sondern modifizieren die Liste
del(f[0]) #entfernt per index

#Setzt eine Referenz
b = a
#Kopiert die Liste
b = list(a)


