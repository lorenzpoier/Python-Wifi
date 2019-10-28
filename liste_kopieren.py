#Listen werden mit eckigen Klammern initialisiert
#Listen mit Beistrich beenden, ist möglich und gewünscht

a = [
    1,
    2,
    3,
    ]
#erstellt nur eine referenz auf die liste    
b = a
#erstellt eine kopie der liste
b = list(a)
 
a.append(4)
 
print(b)
 
l = [0] *10
k = [None] * 10
print(k,l)