# Netreo API cURL Commands for bash shell
Collection of cURL commands for use with the Netreo API
In the supplied examples we use HTTPS

To use these commands you will have to replace:
  - YOUR_SERVER_HERE with your server name or IP
  - YOUR_API_KEY_HERE with the API key you have setup on your instance of Netreo
  - YOUR_DEVICE_NAME_HERE where applicable this will be the name of the device in Netreo that you want data for

### Device Info API 
Retrieves the Netreo metadata for a specific monitored device. Example output

    {
      "result": "completed",
      "name": "Boston-R1",
      "device_index": "40178",
      "description": "Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(3)M5, RELEASE SOFTWARE (fc1) Technical Support:
               http://www.cisco.com/techsupport Copyright (c) 1986-2016 by Cisco Systems, Inc. Compiled Tue 09-Feb-16 06:35 by prod_rel_team",
      "category": "Site Routers",
      "site": "Boston",
      "related_strategic_groups": [
        "Infrastructure",
        "Core Routers"
      ],
      "device_documentation": {
        "16939": {
          "name": "Support_Contract",
          "value": "12345"
        },
        "16940": {
          "name": "Circuit_ID",
          "value": "A92847-2123-54251B-123"
        },
        "reference_contact": {
          "10433": {
            "Contact Email": "manager.branch123@customer.com",
            "Contact Number": "949-555-1212",
            "Contact Name": "Branch Manager"
          }
        }
      }
    }
    
    
    
