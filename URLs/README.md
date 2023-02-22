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

Show Failed logons to Netreo - basically get the Audit Log with filters - there are many ways to do this as well as with the API. In case you need to just do a URL, here is the format. **NOTE:** there is a value (use_date) that you need to change to month, day, year in the format of:

     month 2 digit (March would be = 03
     day is 2 digits (so the 4th would = 04
     year is 4 digits (2022 or your 4 digit year)
     Put together use_date = 03/04/2022

The URL presented here is for Failed Logons from use_date and 90 days forward. This means if you want the last 90 days from say 12/01/2023 you would have a use_date of 09/01/2023. this url does not go backwards 90 days it goes forward from the use_date. **REPLACE use_date with correct date format**

     Audit Log - Failed Logons
     - /admin/audit_log.php?device_name=&user=&edit_location=&message=login+failure&time_option=1&start_time=" + use_date + "+12:00+am&report_time=90dy&result_limit=1000&display_option=html&does_not_match=&submit_report=Get+Audit+Log
