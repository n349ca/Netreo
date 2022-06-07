# Netreo
Collection of Python Scripts for use with the Netreo API
There are different python scripts to support Netreo API access.
These were developed on Python 3.x
Executables must be run from from a command line window
For Windows 10 and 11
1. Click on your windows start menu (or press your windows button on the keyboard)
2. Type **CMD** and hit enter
3. Inside the Command Window go to where you saved the EXE files and run them from there

## Netreo API Tools 
These are Python scripts and fully executable programs on windows machines that utilize the Netreo API.
You will find a variety of different tools available. With the list growing regularly.

### POST_Active_Incidents.py 
Python program will access the Netreo API and pull all the active incidents
While pulling the incidents both Category and Site (in incident api) are numbers
The script will accesses Category and Site API to pull all of those for reference
Next the script looks up the references for Category and Site
Finally writing to CSV the output 
All saved into c:\temp (a windows based directory) with the time of days in the file name

### Excel_POST_Active_Incidents.py
This script is the same as GET_Active_Incidents.py with the exception of adding 2 more columns of data
In Excel these would be Column G (7) & H (8)
Column G adds todays date and time that the program was run
Column H is a calculation for how long the incident has been active

### Post_Audit-Log.py
Exports the Netreo audit log to CSV format into C:\Temp directory (windows)
Script allows for lasthr, 24hr or, 7dy timeframes
Takes into account SaaS or appliance systems and on appliances
    takes into account API Key or no Key

