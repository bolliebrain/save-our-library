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


def clear():
    """
    clear the screen
    """
    print('\033c')


def see_donations(total_donations, details_name_worksheet):
    """
    Prints all donations and associated messages input by user
    """

    calculate_total(details_name_worksheet, total_donations)

    total_messages = details_name_worksheet.col_values(3)[1:]

    for i in range(len(total_donations)):
        print('£' + total_donations[i] + '\t' + total_messages[i])


def get_name_data():
    """
    Gets name input from user after passing validation
    """

    data_name = " "
    print("Lets start by telling us who this donation is from...")
    print("You can also make this anonymous, simply type Anonymous\n")

    while True:
        data_name = input("Enter your name here: \n")

        if validate_name_data(data_name):
            break

    return data_name


def validate_name_data(data_name):
    """
    Validates data to make sure no numbers or symbols are input
    Prints name back to user
    """

    if any(char.isdigit() for char in data_name):
        print("Error: Name cannot be blank or contain numbers or symbols.")
        return False
    elif not data_name.isalnum():
        print("Error: Name cannot be blank or contain numbers or symbols.")
        return False
    elif type(data_name) == str:
        print(f"Thank you, this Donation is from {data_name}\n")
        return True


def get_donation_data():
    """
    Gets donation input from user after passing validation
    """

    donation_amount = 0

    while True:
        print("How much would you like to Donate to Save our Library?")
        print("Enter an amount below (rounding your donation to the pound)")
        donation_amount = input("I would like to donate £")

        if validate_donation_data(donation_amount):
            break

    return donation_amount


def validate_donation_data(donation_amount):
    """
    Validate data to make sure numbers only are input
    Prints data back to user
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
    If message is blank without spaces, Anonymous is automatically input
    """

    message_data = " "
    print("Feel free to leave a message on our wall for people to see")
    message_data = input("Message: ")

    if len(message_data) == 0:
        return "Anonymous"

    return message_data


def thank_you(data_name, donation_amount, message_data):
    """
    prints name, donation and message back to user
    """

    print(f"We have another donation of £{donation_amount} from {data_name}")
    print(f"...{message_data}\n")


def update_worksheet(data_name, donation_amount, message_data, details_name_worksheet):
    """
    update details worksheet to add a new row with name, donation
    and message data. Cuts characters after 50 for name and message.
    """

    print("...updating details\n")

    all_data = [data_name[:50], int(donation_amount), message_data[:50]]

    details_name_worksheet.append_row(all_data)
    print("Added details with data successfully\n")


def calculate_total(details_name_worksheet, total_donations):
    """
    calculating total raised column, removing the first value
    """

    total_raised = 0

    for val in total_donations:
        total_raised += int(val)

    print(f"So far we have raised....£{total_raised}!\n")
    return


def main():
    while True:
        clear()
        print("Save our local Library\n")
        print("More and more libraries are closing every year...\n")
        print("We are raising money to keep our local library open\n")
        print("What would you like to do today?\n")
        print("Option 1 - I would like to Donate\n")
        print("Option 2 - I would like to see Donations\n")
        print("Option 3 - Exit\n")

        """
        worksheet variable
        """
        details_name_worksheet = SHEET.worksheet("details")

        menu_option = input("Option... \n")
        if menu_option == '1':
            clear()
            data_name = get_name_data()
            donation_amount = get_donation_data()
            message_data = get_message()

            thankyou = thank_you(data_name, donation_amount, message_data)
            update_worksheet(data_name, donation_amount, message_data, details_name_worksheet)

            total_donations = details_name_worksheet.col_values(2)[1:]
            all_donations = calculate_total(details_name_worksheet, total_donations)
            input('Press any button to take you back to the menu...\n')

        elif menu_option == '2':
            clear()
            total_donations = details_name_worksheet.col_values(2)[1:]
            see_donations(total_donations, details_name_worksheet)
            ("\n")
            input('Press any button to take you back to the menu...\n')

        elif menu_option == '3':
            clear()
            print("Thanks for visiting... Come back again soon!")
            break

        else:
            print("Error: select 1 or 2 or 3")
            input('Press Enter to continue...\n')


main()
