# Description

This library lets you export 2D arrays of data into your Google Spreadsheet.

The following code snippet will export "Name" and "David" into your Google Spreadsheet,
assuming you are all set up on the Google Cloud side.

If this is not the case, continue to the section 'Complete Guide'

## Quickstart:

Install the library by running
`pip install google-spreadsheets-exporter`

Include the following code snippet for desired functionality

      from pathlib import Path
      from google_spreadsheets_exporter.exporter import Exporter
        
      BASE_DIR = Path(__file__).resolve() # adjust path to your credentials file filder as needed
      data = [["Name"],["David"]]
        
      exp = Exporter("spreadsheet-id", "sheet-name", data, credentials_file_full_path=os.path.join(BASE_DIR, "creds.json"))
      exp.export()

## Complete Guide

- Step 1: Set up a Google Sheets API Project

    - Go to the Google Developers Console (https://console.developers.google.com/) and create a new project.
      - A user for this project has to be created. Note its email.
    - Enable the Google Sheets API for your project.
    - Create credentials for your project to access the API. For this purpose, you'll need a service account key, which is a JSON file containing authentication information.
      - Alternatively you can provide all credentials in a dictionary. For more on this - refer to the "Authenticating with dictionary of credentials" seciton.
    - The credentials JSON file should be downloaded and included in your project.


- Step 2: 
    - Create a Google sheet from your account
    - Note down Spreadsheet ID
      - eg https[]()://docs.google.com/spreadsheets/d/<font color="green">*spreadsheetId-sdvs-dsv*</font>/edit#gid=0/
    - Share the Spreadsheet with the email of your newly created Google project user.
  

- Step 3: Include this code snippet in you project
    - Install the library by running
      `pip install google-spreadsheets-exporter`
        
      Include the following code snippet for desired functionality
        ````
      from pathlib import Path
      from google_spreadsheets_exporter.exporter import Exporter
        
      BASE_DIR = Path(__file__).resolve() # adjust path to your credentials file filder as needed
      data = [["Name"],["David"]]
        
      exp = Exporter("spreadsheet-id", "sheet-name", data, credentials_file_full_path=os.path.join(BASE_DIR, "creds.json"))
      exp.export()

    where `spreadsheet-id` and `sheet-name` has been extracted from Spreadsheet url, `data` is 2D python array and
    `credentials_file_full_path` is full path to your credentials file.


### Authenticating with dictionary of credentials

- You will need to assemble the dictionary of credentials that will match the JSON credentials file.
    
Sample dictionary:
````
credentials_info = {
    "type": "service_account",
    "project_id": "your-project-id",
    "private_key_id": "your-private-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
    "client_email": "your-service-account-email@your-project-id.iam.gserviceaccount.com",
    "client_id": "your-client-id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account-email%40your-project-id.iam.gserviceaccount.com"
}
````

- *Usecase*: Assumed use-case is that the JSON credentials file is downloaded from Google Cloud project
  and for some reason is disassembled and is put back together at runtime. 

- Once you assemble the dictionary of credentials, you will initialize the Exporter class like so:

    `exp = Exporter("spreadsheet-id", "sheet-name", data, using_credentials_file=False, credentials_dictionary=my_assembled_dict))`


Happy exporting.