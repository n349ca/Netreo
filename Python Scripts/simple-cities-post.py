import requests
import json

pswd = 'ENTER YOUR NETREO API KEY HERE (not for SaaS systems)'

response = requests.post('https://ENTER.YOUR.SERVER.HERE/fw/index.php?r=restful%2Fsite%2Flist', json={'password' : pswd})

print(response.status_code)

r = response.json()
print(r)
