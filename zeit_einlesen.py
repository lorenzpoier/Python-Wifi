'''zeit_einlesen


'''
import datetime

date_from_datebase = "1956-02-23"
# (1956, 2, 23)

year = date_from_datebase[0:4]
month = date_from_datebase[5:7]
day = date_from_datebase[8:]

date_elements = date_from_datebase.split('-')
print(date_elements)
#als integer konvertieren
[y,m,d] = [int(x) for x in date_from_datebase.split('-')]
print(date_elements)

print(y, m, d)
birth_day_date = datetime.date(y, m, d)
print( day, month, year)

