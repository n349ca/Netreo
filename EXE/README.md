# Netreo EXE Windows Executables
Collection of Python scripts converted to executables for use with the Netreo API.
All EXE executables use HTTPS.
You must first open a command prompt window and then run the EXE files.

Confirm you have a diretory __C:\Temp__ if not create it, all routines use this diretory.

### addDeviceImportCSV.exe
You have to use the CSV files found on GitHub with this program.

Rules for Data Entry

      1. Required Fields
                IP address
                SNMP Pub (community string)
                Poll  (either 0=do not poll or 1=enable device polling)
                Enable (either 0=do not enable or 1=enable device)
        2. Use the correct template (CSV File) for either On Prem or Saas based
              addDevicesImport(OnPrem).csv
              addDevicesImport(SaaS).csv
        3. Fill in all appropriate data (make sure you have the required fields populated)
        4. Delete the header (Row 1) & sample data if you left it there
        5. Save as a CSV file
        6. CSV file location expected to be c:\Temp\testFile.csv (change as appropriate)

    Top line of CSV files (row 1) is the header row
    Row 2 is sample data - delete this and add your own
    Run the executable (Python) program called --- addDeviceImportCSV.exe

### API-POST_active_incidents.exe
Built from the python program will access the Netreo API and pull all the active incidents. 
While pulling the incidents both Category and Site (in the incident api) are numbers. 
The script will then access both Category and Site APIs to pull all of those for reference. 
Next the script looks up the references for Category and Site. 
Finally writing everything out to a CSV output file.
All saved into c:\temp (a windows based directory) with the time of days in the file name

### Excel_POST_Active_Incidents.exe
This executable is the same as API-POST_active_incidents.exe with the exception of adding 2 more columns of data
In Excel these would be Column G (7) & H (8)
Column G adds todays date and time that the program was run
Column H is a calculation for how long the incident has been active

### site-list.py
Exports Netreo list of Sites to a CSV format into C:\temp directory (windows)
EXE will use SaaS or appliance based systems with or without the API Key.

### category-list.py
Exports Netreo's list of Categories to a CSV format into C:\temp directory (windows)
EXE will use SaaS or appliance based systems with or without the API Key.
