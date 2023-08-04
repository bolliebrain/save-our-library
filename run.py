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
            update_name(data_name)
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
        print(f"Thank you, this Donation is from {data_name}\n")
        return True
        
def update_name(data_name):
    """
    update details worksheet to add a new row with name data
    """

    print("Adding name to profile")
    details_name_worksheet = SHEET.worksheet("details")
    details_name_worksheet.append_row(data_name)
    print("Added name successfully")

def get_donation_data():
    """
    Get donation input from user
    """
    donation_amount = 0

    while True:
        print("How much would you like to Donate to Save our Library?")
        print("Enter an amount below, we would appreciate you rounding your donation to the pound")
        donation_amount = input("I would like to donate £")
        
        if validate_donation_data(donation_amount):
            break

def validate_donation_data(donation_amount):
    """
    Validate data to make sure numbers are input only
    """

    if not donation_amount.isdigit():
        print("Error: please enter amount in numbers only")
        return False
    elif type(donation_amount) == str:
        print(f"You have donated £{donation_amount}")
        return True

def get_message():
    """
    Get message input from user
    """
    message_data = " "
    print("Feel free to leave a message on our wall for people to see")
    message_data = input("Message: ")

    if message_data:
        print("thankyou")



get_name_data()

get_donation_data()

get_message()

