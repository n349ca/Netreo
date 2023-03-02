# Hidden URLs found in Netreo

There are a collection of URLs that are not documented but are very useful when you need specific data that the API does not provide. Many of these links provide JSON formated output, which is excelent for other tools to access Netreo. For instance if you wanted to have ServiceNow or SPLUNK access data in Netreo. The list of URL's below are only what have been found through trial and error and researching the HTML of the page.

As you find new URL's please add them to this list to help others!!!

***NOTE:*** the URLs below are partial URLs meaning that they would be placed after your Netreo server name. For instance https://netreo.lap.com would be your server name and then you would add to this a URL from below. 

This one has a ton of debug info and is a complex Debug page. 

     Netreo Debug Page (click on Status 200 to expand the full menu)
     - /fw/index.php?r=debug/default/index

Capture service Engines in Netreo - JSON formatted

     Service Engine List
     - /fw/index.php?r=device-management/get-device-stats-by-group&group_type=service_engine

Capture all devices in Netreo - JSON formatted (not tested on large environments)

     All Device List
     - /fw/index.php?r=device-management/get-device-stats-for-group&group_type=oc&group_id=null
     
Capture Strategic Group Page - JSON formatted

     Strategic Group List
     - /fw/index.php?r=strategic-group/get-strategic-groups
     
     Aggregate Strategic Group List
     - /fw/index.php?r=aggregate-strategic-group/admin-list

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

Disabled Devices in Netreo - JSON formatted

     Managed Disabled Devices
     - /fw/index.php?r=device-management/disabled-devices&data_only=1"
     
     Unmanaged Disabled Devices (were not managed yet)
     - https://demo.netreo.com/fw/index.php?r=device-management/disabled-devices&data_only=0&unvalidated=1
     
Unlocked Thresholds report - JSON formated

     Unlocked thresholds
     - /fw/index.php?r=report/unlock-thresholds&data_only=1

Service Engines - JSON formatted

     Service Engines List
     - /fw/index.php?r=oc-remote-resource/get-service-engines
     
     Service Engine Groups
     - /fw/index.php?r=oc-remote-resource/get-service-engine-groups
     
     Don't have a way to test these but think they should work
     NetFlow / sFlow data
     - /fw/index.php?r=oc-remote-resource/get-flows
     
     Log data for the last 10
     - /fw/index.php?r=log/log-last-ten

Remote Agent List with basic information - JSON formatted

     Remote Agents 
     - /fw/index.php?r=oc-remote-resource/get-remote-agents
     
Configuration URLs - JSON formatted 

     Configuration Compliance Exceptions
     - /fw/index.php?r=cfg-mgr/get-config-templates&time_option=1&exception_option=1&report_time=90d
     
     Configuration Authentication Failure (can't logon to get the configuration)
     -/fw/index.php?r=cfg-mgr/get-auth-fails&device_id=

Show Failed logons to Netreo - basically get the Audit Log with filters - there are many ways to do this as well as with the API. In case you need to just do a URL, here is the format. 

The URL presented here is for Failed Logons for the last 90 days. 

     Audit Log - Failed Logons
     - /admin/audit_log.php?device_name=&user=&edit_location=&message=login+failure&time_option=1&report_time=90dy&result_limit=1000&display_option=html&does_not_match=&submit_report=Get+Audit+Log
