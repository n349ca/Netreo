import json
import requests

# Set the baseAPI variable to the API string needed (in this case delete a device)  
#-----------  Enter the API string ---------------------
baseAPI = '/api/device_delete_api.php'

# ask for input 
# get the Netreo server name or the ip address 
input_url = input("Please enter Netreo server name or IP: ")
# if there is not a key then use customized url 
input_saas = input("Are you using Netreo SaaS (y/n): ")

if input_saas.lower() == "n":
	input_key = input("Enter your API key (if not used type 'none'): ")
	if input_key.lower() == "none":
	    baseURL = "https://" + input_url + baseAPI
	else:
	    baseURL = "https://" + input_url + baseAPI + '?pwd=' + input_key
else:
    # If using SaaS system then change pwd to pin and setup the URL
    # https://xyz.com/api/new_device_api.php?pwd=vvvvv&snmp_pub=zzzz&ip=1.1.1.2&poll=1&enabled=1
	input_key = input("Enter the SaaS Pin: ")
	baseURL = "https://" + input_url + baseAPI + '?pin=' + input_key

    # enter the name of the device you want to delete
    # you must use the exact name used in netreo or the ip address
    # then add that to the baseURL 
	deleteDeviceName = input("Enter the full device name or IP to delete from Netreo: ")
	baseURL = baseURL + '&name=' + deleteDeviceName

	# -----   
    # Perform the URL post 
    data = requests.post(baseURL)
    try:
    	print(data.json())
    except Exception:
    	pass

    if data.status_code != 200:
	    print('API did not respond correctly, please confirm:')
	    print('    1. that you have the API turned on in Netreo')
	    print('    2. you need or do not need an API key')
	    print('    3. when you entered the API key it was correct')
	    print('    4. If using SaaS confirm your Pin was correct')
	    exit()
