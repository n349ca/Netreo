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

# enter the time period that we need to retrieve from Netreo
# setup the specific times that we will allow
timeVals = ("lasthr", "24hr", "7dy")
input_timePeriod = input("What Time Period (lasthr, 24hr, 7dy): ")
if input_timePeriod.lower() not in timeVals:
	print('\n\nYou did not select a correct Time Period.')
	exit()

if input_saas.lower() == "n":
	input_key = input("Enter your API key (if not used type 'none'): ")
else:
	input_key = input("Enter the SaaS Pin: ")


#print(url_incidents)

# POST a call to server
# put the result into data

# If using SaaS system then change pwd to pin and setup the URL
if input_saas.lower() == "n":
	if input_key.lower() == "none":
		url_auditLog = "https://" + input_url + "/fw/index.php?r=restful%2Faudit-log%2Flog-list"
		data = requests.post(url_auditLog, json={'timeperiod' : input_timePeriod})
	else:
		url_auditLog = "https://" + input_url + "/fw/index.php?r=restful%2Faudit-log%2Flog-list"
		data = requests.post(url_auditLog, json={'timeperiod' : input_timePeriod, 'password' : input_key})
else:
	data = requests.post(url_auditLog, json={'timeperiod' : input_timePeriod, 'pin' : input_key}) 
# checking the status code of the request
#print(data.json())
#exit()

if data.status_code == 200:
	data_auditLog = data.json()
	print('\n\nData for Audit Log collected')
	#print(data_auditLog)	
else:
	print('Audit Log API did not respond correctly, please confirm:')
	print('    1. that you have the API turned on')
	print('    2. you need or do not need an API key')
	print('    3. when you entered the API key it was correct')
	print('    4. If using SaaS confirm your Pin was correct')
	exit()


# Returns the current local date
today = str(date.today())

# This will be the CSV header row (first line of CSV)
header = ["Time", "Device", "User", "Location", "Message"]
# open the file in the write mode
#-------------Change Directory from C:\\temp to your specific directory (linuix or windows) -----------
opn = "C:\\temp\\Audit-Log" + today + ".csv"
#print(opn4)
g = open(opn, 'w', newline='')

# create the csv writer
writer = csv.writer(g)
writer.writerow(header)

# Loop through the active incidents from Data_Incident
for logData in data_auditLog:
	print(logData)
	time = logData['time']
	device = logData['device']
	user = logData['user']
	location = logData['location']
	msg = logData['message']
	
	#openTime = logData['open_time']
	#time = openTime.replace("T", " ")

	#print(state, title, category, site)
	# send the data out to the CSV
	export = [time, device, user, location, msg]
	writer.writerow(export)

print('-------------------------------------')
print('CSV file saved to ' + opn)
