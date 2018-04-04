import requests
import shelve


api_key= "RGAPI-19ee180c-0a2e-46be-8f6d-f8addf83999c"

url = "https://na1.api.riotgames.com/lol/static-data/v3/champions"
url += "?api_key=" + api_key
response = requests.get(url)
data = response.json()

#print (data['data']['Orianna']['title'])
s = shelve.open('Static_Champion_Data', writeback=True)
try:
    for key in data['data']:
        s[key] = data['data'][key]
finally:
    s.close()

