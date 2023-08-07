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


def welcome():
    print("Save our local Library\n")
    print("More and more libraries are closing every year...\n")
    print("We are raising money to keep our local library open\n")
    print("What would you like to do today?\n")
    print("Option 1 - I would like to Donate\n")
    print("Option 2 - I would like to see Donations\n")

    menu_option = 0

    while True: 
        menu_option = input("Option... ")

        if validate_option(menu_option):
            break

def validate_option(menu_option):
    """
    check that option answer is 1, 2 or 3
    """
    """
    menu_option == '2':
    """
    if menu_option == '1':
        return True
    else:
        print("Error: select 1, 2 or 3")
        return False

def get_name_data():
    """
    Get name input from user
    """
    data_name = " "
    print("Lets start by telling us who this donation is from...")
    print("You can also make this anonymous, simply type Anonymous\n")

    while True:
        data_name = input("Enter your name here: ")
        
        if validate_name_data(data_name):
            break
    
    return data_name

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

    return donation_amount

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
    
    return donation_amount

def get_message():
    """
    Get message input from user
    """
    message_data = " "
    print("Feel free to leave a message on our wall for people to see")
    message_data = input("Message: ")

    return message_data

def thank_you(data_name, donation_amount, message_data):

    print(f'We have another donation of £{donation_amount} from {data_name}')
    print(f'...{message_data}')

    """
    print('Our total amount raised is .....')
    print('Drum roll please...')
    print(Calculate amount)


"""
def update_worksheet(data_name, donation_amount, message_data):
    
    update details worksheet to add a new row with name data
    
    return data_name
    return donation_amount
    return message_data

    all_data = data_name + donation_amount + message_data
    print(all_data)

    results = []
    results.append(all_data)
    print(results)
    details_name_worksheet = SHEET.worksheet("details")
    details_name_worksheet.append_row(results)
    print("Added data successfully")
"""

def main():
    """
    update_worksheet()
    """
    
    welcome()
    
    name = get_name_data()
    data_name = [name]

    donation = get_donation_data()
    donation_amount = [donation]

    message = get_message()
    message_data = [message]
    
    thankyou = thank_you(data_name,donation_amount,message_data)


main()
