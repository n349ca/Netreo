import requests
import json

pwd = 'ENTER YOUR NETREO API KEY HERE (not for SaaS systems)'
response = requests.post('https://ENTER.YOUR.SERVER.HERE/fw/index.php?r=restful%2Fcategory%2Flist', json={'password' : pwd})

print(response.status_code)

r = response.json()
print(r)
