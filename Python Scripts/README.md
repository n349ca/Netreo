# Netreo Python Scripts
Collection of Python Scripts for use with the Netreo API
All scripts and executables use HTTPS

Must install **json**, **requests**, and **csv** in python

      1. Open a command line window 
      2. change to your python directory
      3. type - pip install csv
      4. type - pip install json
      5. type - pip install requests
    
There are different python scripts to support Netreo API access.
Executables were developed on Python 3.x
Executables must be run from from a command line window
For Windows 10 and 11
1. Click on your windows start menu (or press your windows button on the keyboard)
2. Type **CMD** and hit enter
3. Inside the Command Window go to where you saved the EXE files and run them from there

## Netreo API Tools 
These are Python scripts written for version 3.x Python. 
Windows executable programs can also be found in this repository. 
You will find a variety of different tools available. With the list growing regularly.

### POST_Active_Incidents.py 
Python program will access the Netreo API and pull all the active incidents. 
While pulling the incidents both Category and Site (in the incident api) are numbers. 
The script will then access both Category and Site APIs to pull all of those for reference. 
Next the script looks up the references for Category and Site. 
Finally writing everything out to a CSV output file.
All saved into c:\temp (a windows based directory) with the time of days in the file name

### Excel_POST_Active_Incidents.py
This script is the same as POST_Active_Incidents.py with the exception of adding 2 more columns of data
When importing the CSV to Excel these would be Column G (7) & H (8)

    Column G adds todays date and time that the program was run
    Column H is a calculation for how long the incident has been active

### Post_Audit-Log.py
Exports the Netreo audit log to CSV format into C:\Temp directory (windows)
Script allows for lasthr, 24hr or, 7dy timeframes
Takes into account SaaS or appliance systems and on appliances it 
    takes into account the API Key or no Key

### site-list.py
Exports Netreo list of Sites to a CSV format into C:\temp directory (windows)
Script will use SaaS or appliance based systems with or without the API Key.

### category-list.py
Exports Netreo's list of Categories to a CSV format into C:\temp directory (windows)
Script will use SaaS or appliance based systems with or without the API Key.

### addDeviceImportCSV.py
You have to use the CSV files with this program
Rules for Data Entry

      1. Required Fields
                IP address
                Poll  (either 0=do not poll or 1=enable device polling)
                Enable (either 0=do not enable or 1=enable device)
        2. Use the correct template (CSV File) for either On Prem or Saas based
              addDevicesImport(OnPrem).csv
              addDevicesImport(SaaS).csv
        3. Fill in all appropriate data (make sure you have the required fields populated)
        4. Delete the header (Row 1) & sample data if you left it there
        5. Save as a CSV file
        6. CSV file location expected to be c:\Temp\testFile.csv (change as appropriate)

    Top line of CSV files (row 1) is the header row useful during population of data (and is deleted before use)
    Row 2 is sample data - delete this and add your own
    Run the Python program called --- addDeviceImportCSV.py

