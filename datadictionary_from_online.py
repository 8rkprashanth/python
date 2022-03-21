from urllib import response
import requests
response = requests.get("http://api.open-notify.org/astros.json")
#print(response)
json=response.json()#
#print(json)
for person in json["people"]:
    print(person["name"])