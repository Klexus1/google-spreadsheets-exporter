from django.conf import settings

# Define the default credentials file path
DEFAULT_CREDENTIALS_FILE_PATH = 'credentials.json'

# Function to load credentials from a specified file path or the default path
def load_google_credentials():
    credentials_file_path = getattr(settings, 'GOOGLE_SPREADSHEET_CREDENTIALS_FILE_PATH', DEFAULT_CREDENTIALS_FILE_PATH)
    json_key_path = os.path.join(os.path.dirname(__file__), credentials_file_path)
    return service_account.Credentials.from_service_account_file(json_key_path)