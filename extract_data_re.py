import re
address = 'Schulgasse 234; 1090 gars am kamp, Stiege
27'
#4 ziffern hintereinander werden in einem output geliefert
data = re.search(r'(\d{4})', address)
print(data.group(1))


#4 ziffern hintereinander werden in 2 outputs geliefert
data = re.search(r'(\d{2})(\d{2})', address)
print(data.group(1))
print(data.group(2))

#\1 oder mehr zeichen mit gasse als string wird gespeichert
data = re.search(r'(\w+gasse)', address)
print(data.group(1))
