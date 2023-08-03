import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('save_our_library')

def get_name_data():
    """
    Get name input from user
    """
    print("Lets start by telling us who this donation is from...")
    print("You can also make this anonymous, simply type Anonymous\n")
    
    data_name = input("Enter your name here: ")
    print(f"the data provided is {data_name}")

get_name_data()