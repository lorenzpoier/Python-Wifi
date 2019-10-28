'''
Umgang mit Datumsformaten

'''

import datetime
import time	


#system zeit in jahr monat tag h:min:sec
print(datetime.datetime.now())

#epoch ist beginn der unix zeit
print(time.time())
epoch = time.time()
print(datetime.datetime.fromtimestamp(epoch))
epoch = 4294967296
print(datetime.datetime.fromtimestamp(epoch))
epoch = 0
print(datetime.datetime.fromtimestamp(epoch))

#iso 8601: YYYY-MM-DD

birth_day = (1975,2,23,4,0,0, 0, 0 , 0)
birth_day_dt = time.mktime(birth_day)
print(birth_day_dt)

birth_day_date = datetime.date(1975,2,23)
print(birth_day_date)
today_date = datetime.date.today()
print(today_date - birth_day_date)

diff = (today_date - birth_day_date )
print(diff.days)
print(diff.days/365.24)

