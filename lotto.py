'''
ziehen der lotto zahlen
6 zufallszahlen aus 45
ohne zurücklegen

mit Listenoperationen
mit python funktionen
'''
import time
import random

anzahl_lottozahlen = 6
max_lottozahl = 45

start_time = time.time()
i = 1
gezogene_lottozahlen = []
neue_iteration = 0
while i <= anzahl_lottozahlen:
    gezogene_lottozahlen.append(random.randint(1, max_lottozahl + 1)) 
    for j in range(i):
        if gezogene_lottozahlen[-1] == gezogene_lottozahlen[j] & i != 1:
            neue_iteration = 1
    if neue_iteration == 0:
        i += 1
    else:
        neue_iteration == 0
        
print(gezogene_lottozahlen)
#elapsed_time = time.time() - start_time
print(elapsed_time)


start_time = time.time()
count = anzahl_lottozahlen
max_number = max_lottozahl + 1
lotto_numbers = []
while len(lotto_numbers) < count:
    zz = random.randint(1, max_number)
    if zz not in lotto_numbers:
        lotto_numbers.append(zz)
#print(lotto_numbers)
elapsed_time = time.time() - start_time
print(elapsed_time)


start_time = time.time()
#print("Lottozahlen: ", random.sample(range(1,max_lottozahl + 1), anzahl_lottozahlen))
elapsed_time = time.time() - start_time
print(elapsed_time)

start_time = time.time()
lottozahlen = [x for x in range(1, max_lottozahl+1)]
gezogene_lottozahl = []
for i in range(anzahl_lottozahlen + 1):
    gezogene_lottozahl.append(random.choice(lottozahlen))
    lottozahlen.remove(gezogene_lottozahl[i])
#print(gezogene_lottozahl)
elapsed_time = time.time() - start_time
print(elapsed_time)


start_time = time.time()
lottozahlen = [x for x in range(1, max_lottozahl+1)]
max_index = max_lottozahl
gezogene_lottozahl = []
for i in range(0, anzahl_lottozahlen):
    gezogene_indexzahl = random.randint(0, max_index - i -1)
    gezogene_lottozahl.append(lottozahlen[gezogene_indexzahl])
    del(lottozahlen[gezogene_indexzahl])
#print(gezogene_lottozahl)
elapsed_time = time.time() - start_time
print(elapsed_time)

