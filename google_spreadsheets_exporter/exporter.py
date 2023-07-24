from google.oauth2 import service_account
from googleapiclient.discovery import build


def load_credentials_from_file(credentials):
    return service_account.Credentials.from_service_account_file(credentials)


def load_credentials_from_dictionary(credentials):
    return service_account.Credentials.from_service_account_info(credentials)


class Exporter():
    def __init__(self,
                 spreadsheet_id:str,
                 list_name:str,
                 data:list,
                 using_credentials_file:bool=True,
                 credentials_file_full_path="credentials.json",
                 credentials_dictionary=None):

        super().__init__()
        if credentials_dictionary is None:
            credentials_dictionary = {}

        self.spreadsheet_id = spreadsheet_id
        self.list_name = list_name
        self.data = data
        self.using_credentials_file = using_credentials_file
        self.creds_file_path = credentials_file_full_path
        self.credentials_dictionary = credentials_dictionary

        if using_credentials_file:
            self.credentials = load_credentials_from_file(credentials_file_full_path)
        else:
            self.credentials = load_credentials_from_dictionary(credentials_dictionary)

    def export(self):
        print("exporting data ..")
        service = build('sheets', 'v4', credentials=self.credentials)

        # Spreadsheet ID - Obtain this from the URL of your Google Sheet
        spreadsheet_id = self.spreadsheet_id

        # Define the range where you want to insert the data (e.g., 'Sheet1!A1')
        range_name = self.list_name

        # Call the Sheets API to insert the data into the Google Sheet
        result = service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption='RAW',
            body={'values': self.data}
        ).execute()

        print(f"{result.get('updatedCells')} cells updated.")