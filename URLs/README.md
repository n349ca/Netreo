# Hidden URLs found in Netreo

There are a collection of URLs that are not documented but are very useful when you need specific data that the API does not provide. Many of these links provide JSON formated output, which is excelent for other tools to access Netreo. For instance if you wanted to have ServiceNow or SPLUNK access data in Netreo. The list of URL's below are only what have been found through trial and error and researching the HTML of the page.

As you find new URL's please add them to this list to help others!!!

***NOTE:*** the URLs below are partial URLs meaning that they would be placed after your Netreo server name. For instance https://netreo.lap.com would be your server name and then you would add to this a URL from below. 

Capture service Engines in Netreo - JSON formatted

     Service Engine List
     - /fw/index.php?r=device-management/get-device-stats-by-group&group_type=service_engine

Capture all devices in Netreo - JSON formatted (not tested on large environments)
     All Device List
     - /fw/index.php?r=device-management/get-device-stats-for-group&group_type=oc&group_id=null
     
Capture Strategic Group Page - JSON formatted
     Strategic Group List
     - /fw/index.php?r=strategic-group/get-strategic-groups

List of Categories
     Category Group page
     - /fw/index.php?r=category/sindex

Current version and possible upgrade version of Netreo
     Version of Netreo
     - /ajax/omnicenter_software_update_ajax.php?check=1

Device Managment Page (by different groupings) - JSON formatted
     By Category
     - /fw/index.php?r=device-management/get-device-stats-by-group&group_type=category
     
     By Device Type
     - /fw/index.php?r=device-management/get-device-stats-by-group&group_type=type
     
     By SubType
     - /fw/index.php?r=device-management/get-device-stats-by-group&group_type=sub_type
     
     By Site
     - /fw/index.php?r=device-management/get-device-stats-by-group&group_type=site
     
     By Strategic Grouping
     - /fw/index.php?r=device-management/get-device-stats-by-group&group_type=strategic_group
     
     
