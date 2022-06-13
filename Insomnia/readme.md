# Insomnia Import File
Insomnia tool may be downloaded from https://insomnia.rest/download

To use this file you will have to replace all references:
* YOUR_SERVER_HERE with your server name or IP
* YOUR_API_KEY_HERE with the Netreo API key
* DEVICE_YOU_WANT_DATA_FOR with an actual device in your Netreo deployment
## Included POST Commands
There are 6 API calls that this file will setup for you in Incomnia
1. POST - Get Incidents (collect all active incidents)
2. POST _ Device Services (get all services for a device and show the status)
3. POST - Category List (List all categories)
4. POST - Audit Log (retrieve the last hour of the audit log)

          Change timeperiod to **lasthr**, **24hr**, or **7dy** for different timeframe
5. POST Strategic Group List (List all strategic groups)
6. POST - Site List (List all sites)
