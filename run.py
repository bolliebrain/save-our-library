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



"""
def welcome():
    Welcome page Save our Library
"""

"""
def options():
    Option 1 - Donate
    Option 2 - See Donations
    Option 3 - Exit
"""


def get_name_data():
    """
    Get name input from user
    """
    data_name = " "

    while True:
        print("Lets start by telling us who this donation is from...")
        print("You can also make this anonymous, simply type Anonymous\n")
        data_name = input("Enter your name here: ")
        
        if validate_name_data(data_name):
            break

def validate_name_data(data_name):
    """
    Validate data to make sure no numbers or symbols are input
    """

    if any(char.isdigit() for char in data_name):
        print("Error: Name cannot contain numbers or symbols.")
        return False
    elif not data_name.isalnum():
        print("Error: Name cannot contain numbers or symbols.")
        return False
    elif type(data_name) == str:
        print(f"Thank you, this Donation is from {data_name}")
        return True
        
get_name_data()
