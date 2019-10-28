a = [ 2, 3, 4]

'''
ein neues Array indem jeder Wert von a um 1 erhöt ist

b = []
for c in a:
    b.append(c + 1)
List Comprehension    

b= [i+1 for i in a]

print(b)
'''

l = [3.4, 5.6, 5.9]
l = [int(x) for x in l ]
print(l)

l = [x for x in range(1, 46)]
print(l)

d = [2] *10
