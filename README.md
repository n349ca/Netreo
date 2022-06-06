# Netreo
Collection of Python Scripts for use with the Netreo API
There are different python scripts to support Netreo API access.

## Netreo API Tools
These are Python scripts and fully executable programs on windows machines that utilize the Netreo API.
You will find a variety of different tools available. With the list growing regularly.

### GET_Active_Incidents.py 
Python program will access the Netreo API and pull all the active incidents
While pulling the incidents both Category and Site (in incident api) are numbers
The script then accesses Category and Site API to pull all of those for reference
Next the script looks up the references for Category and Site
Finally writing to CSV the output 
All saved into c:\temp (a windows based directory)

### Excel_GET_Active_Incidents.py
THis script is the same as with the exception of adding 2 more columns of data
In Excel these would be Column G (7) & H (8)
Column G adds todays date and time the program was run
Column H is a calculation for how long the incident has been active
