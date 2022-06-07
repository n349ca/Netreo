import json
import requests
import csv

# Import date class from datetime module
from datetime import date

# ask for input 
# get the name of the server or the ip address so we can build 
# the URL's to use (there will be 3 - incidents, categories, sites)
input_url = input("Please enter Netreo server name or IP: ")
# if there is not a key then use customized url 
input_saas = input("Are you using Netreo SaaS (y/n)? ")

if input_saas.lower() == "n":
	input_key = input("Enter your API key (if not used type 'none'): ")
else:
	input_key = input("Enter the SaaS Pin: ")

if input_key.lower() == "none":
	url_site = "https://" + input_url + "/fw/index.php?r=restful%2Fsite%2Flist"
	url_category = "https://" + input_url + "/fw/index.php?r=restful%2Fcategory%2Flist"
	url_incidents = "https://" + input_url + "/api/incident_api.php?method_request=getincidents"
else:
	url_site = "https://" + input_url + "/fw/index.php?r=restful%2Fsite%2Flist" 
	url_category = "https://" + input_url + "/fw/index.php?r=restful%2Fcategory%2Flist"

# If using SaaS system then change pwd to pin and setup the URL
if input_saas.lower() == "n":
	url_incidents = "https://" + input_url + "/api/incident_api.php?method_request=getincidents&pwd=" + input_key
else:
	url_incidents = "https://" + input_url + "/api/incident_api.php?method_request=getincidents&pin=" + input_key

#print(url_site)
#print(url_category)
#rint(url_incidents)

# POST a call to server
# put the result into data
#print('Input Key = ', input_key)

# If using SaaS system then change pwd to pin and setup the URL
if input_saas.lower() == "n":
	data = requests.post(url_site, json={'password' : input_key})
else:
	data = requests.post(url_site, json={'pin' : input_key})
# checking the status code of the request
#print(data.json())
#exit()

if data.status_code == 200:
	data_site = data.json()
	print('\n\nData for sites collected')
	#print(data_site)	
else:
	print('Site API did not respond correctly, please confirm:')
	print('    1. that you have the API turned on')
	print('    2. you need or do not need an API key')
	print('    3. when you entered the API key it was correct')
	print('    4. If using SaaS confirm your Pin was correct')
	exit()

# POST a call to server for Category list
# put the result into data
# If using SaaS system then change pwd to pin and setup the URL
if input_saas.lower() == "n":
	data = requests.post(url_category, json={'password' : input_key})
else:
	data = requests.post(url_category, json={'pin' : input_key})

# checking the status code of the request
if data.status_code == 200:
	data_category = data.json()    #json.load(data.content.decode('utf-8'))
	print('Data for Categories collected')
	#print(data_category)
else:
	print('Category API did not respond correctly, please confirm:')
	print('    1. that you have the API turned on')
	print('    2. you need or do not need an API key')
	print('    3. when you entered the API key it was correct')
	print('    4. If using SaaS confirm your Pin was correct')
	exit()

#post the call to incidents API - note this one is different from Site/Category API
data = requests.post(url_incidents)
# checking the status code of the request
if data.status_code == 200:
	data_incident = data.json()
	print('Data for Incidents collected')
	#print(data_incident)
else:
	print('Incidents API did not respond correctly, please confirm:')
	print('    1. that you have the API turned on')
	print('    2. you need or do not need an API key')
	print('    3. when you entered the API key it was correct')
	print('    4. If using SaaS confirm your Pin was correct')
	exit()

# Returns the current local date
today = str(date.today())

# This will be the CSV header row (first line of CSV)
header = ["State", "Title", "Category", "Site", "Date/Time", "Current Time", "Incident Time"]
# open the file in the write mode
opn = "C:\\temp\\incidents_" + today + ".csv"
#print(opn4)
g = open(opn, 'w', newline='')

# create the csv writer
writer = csv.writer(g)
writer.writerow(header)

# Loop through the active incidents from Data_Incident
for incidents in data_incident['active_incidents']:
	#print(incidents)
	title = incidents['title']
	state = incidents['incident_state']
	try:
		category = incidents['device_category']
		#print(category)
		for cat in data_category:
			if cat['id'] == category:
				#print('FOUND CATEGORY ', cat['name'])
				category = cat['name']
	except KeyError:
		category = "Unknown"
	try:
		site = incidents['device_site']
		for sites in data_site:
			if sites['id'] == site:
				#print('FOUND SITE ', sites['name'])
				site = sites['name']
	except KeyError:
		site = "Unknown"
	openTime = incidents['open_time']
	time = openTime.replace("T", " ")

	#print(state, title, category, site)
	# send the data out to the CSV
	export = [state, title, category, site, time, '=NOW()', '=INT(RC[-1]-RC[-2])&" days "&TEXT(RC[-1]-RC[-2],"h"" hrs ""m"" mins """)']
	writer.writerow(export)

print('-------------------------------------')
print('CSV file saved to ' + opn)
