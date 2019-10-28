#Wetter Daten London
# pip install requests
import requests
from pprint import pprint
url = "https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22"

response = requests.get(url)
#delete, get, post, put

data = response.json()

pprint(data)
temp = data['main']['temp']-273.15
pprint('Temperatur: {:0.1f} °C'.format(temp))

