# Netreo Excel VP Scripts (macros)
Collection of VB Scripts for use with the Netreo API
All scripts HTTPS

    To run macros in Excel we recomend
      1. Click the File tab.
      2. Click Options.
      3. Click Trust Center, and then select  Trust Center Settings.
      4. In the Trust Center, click Macro Settings.
      5. Make the selection (typically Disable all macros with Notification)
      6. Click OK.
    Add Required References to VBA
      1. Open VB editor (ALT F11) 
      2. Menu Bar - Tools--> References (opens new window)
      3. Scroll down to Microsoft XML, v 6.0 and check the box
      4. Click OK
      5. Close VB Editor
Scipts should be copied and pasted into Microsoft Excel VB editor (ALT F11)

ALT F8 will bring up the Macro list

## Get Audit Log
This script will retrieve the Netreo Audit Log (last hour, 24 hours, or 7 days)
ALT F8 will bring up the Macro list
Select ThisWorkbook.CaptureAuditLogs or you may only see CaptureAuditLogs 
You will be asked to enter if you use an API key, what the key is, server name or IP, and the time period.
Once completed the script will fill in your worksheet with the Audit log data

