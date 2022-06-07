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
input_saas = input("Are you using Netreo SaaS (y/n): ")

if input_saas.lower() == "n":
	input_key = input("Enter your API key (if not used type 'none'): ")
else:
	input_key = input("Enter the SaaS Pin: ")

# POST a call to server
# put the result into data
url_category = "https://" + input_url + "/fw/index.php?r=restful%2Fcategory%2Flist"
# If using SaaS system then change pwd to pin and setup the URL
if input_saas.lower() == "n":
	if input_key.lower() == "none":
		data = requests.post(url_category)
	else:
		data = requests.post(url_category, json={'password' : input_key})
else:
	data = requests.post(url_category, json={'pin' : input_key}) 
# checking the status code of the request
#print(data.json())
#exit()

if data.status_code == 200:
	data_category = data.json()
	print('\n\nData for Category collected')
	#print(data_auditLog)	
else:
	print('Category List API did not respond correctly, please confirm:')
	print('    1. that you have the API turned on')
	print('    2. you need or do not need an API key')
	print('    3. when you entered the API key it was correct')
	print('    4. If using SaaS confirm your Pin was correct')
	exit()


# Returns the current local date
today = str(date.today())

# This will be the CSV header row (first line of CSV)
header = ["ID", "Name"]
# open the file in the write mode
opn = "C:\\temp\\Category-List-" + today + ".csv"
#print(opn4)
g = open(opn, 'w', newline='')

# create the csv writer
writer = csv.writer(g)
writer.writerow(header)

# Loop through the active incidents from Data_Incident
for categoryData in data_category:
	print(categoryData)
	time = categoryData['id']
	name = categoryData['name']

	#print(time, name)
	# send the data out to the CSV
	export = [time, name]
	writer.writerow(export)

print('-------------------------------------')
print('CSV file saved to ' + opn)
