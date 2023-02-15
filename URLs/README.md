# Hidden URLs found in Netreo

There are a collection of URLs that are not documented but are very useful when you need specific data that the API does not provide. Many of these links provide JASON formated output, which is excelent for other tools to access Netreo. For instance if you wanted to have ServiceNow or SPLUNK access data in Netreo.

***NOTE:*** the URLs below are partial URLs meaning that they would be placed after your Netreo server name. For instance https://netreo.lap.com would be your server name and then you would add to this a URL from below. 

Capture service Engines in Netreo - JSON formated
    '''/fw/index.php?r=device-management/get-device-stats-by-group&group_type=service_engine
