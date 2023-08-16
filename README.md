<h1>Save Our Library</h1>

[View the live project here](https://save-our-library-c912e53ed8f7.herokuapp.com/)

Save Our Library is a command line application to raise funds for local libraries.

The user can interact with the application to make a donation and view other donations made.

The fundraising data is stored in an external Google Spreadsheet.

## Index - Table of Contents
* [User Experience (UX)](#user-experience-ux)
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)

## User Experience (UX)

### User stories - as a used I want to be able to :

1. Easily navigate between the different functions available in the application.
2. Be able to donate.
3. Be able to leave a message with my donation.
4. View other donations and messages.
5. Be able to see how much has been donated.

## Features

### Existing Features

1. Welcome page and menu
- The main menu is displayed when the application starts. To keep it simple to use, the menu is divided into 3 options.
Option 1 - Donate
Option 2 - See Donations
Option 3 - Exit
- The user is prompted to choose one of the menu options by entering a number and if input incorrectly, an error message will be displayed until the user has input a correct option.

![Welcome Menu](documentation/features/01-welcome-menu.png)

2. Donate - Submit Name:
- The Donate - Submit Name is first requested when the user selects Option 1 - Donate.
- The user is prompted to provide a name or type anonymous if they dont want to give their details. If symbols, numbers or blank is input an error message will be displayed until the user has input a correct option.

![Submit Name](documentation/features/02-submit-name.png)

3. Donate - enter amount:
- The Donate - Enter Amount is then requested after the user has provided their name. They are asked to input how much they would like to donate, rounded to the pound. If letters, symbols or blanks are input an error message will be displayed until the user has input a correct option.

![Enter Amount](documentation/features/03-enter-amount.png)

4. Donate - leave a message:
- The Donate - leave a message is finally requested for the user to write anything down that will appear on the wall for viewers to see. This option can be left blank.

![Leave Message](documentation/features/04-leave-message.png)

5. See other donations and messages:
- The user can view all donations and messages that are input retrospectively, including their own once submitted.
- The total raised is also provided.

![See Donations](documentation/features/05-see-donations.png)

- Below is an image of the data that is input into the worksheet:

![Data Input](documentation/features/07-updated-worksheet.png)

6. Exit:
- The user can leave the application completely when finished and will be provided with a message.

![Exit](documentation/features/06-exit.png)

### How these features support the User Stories

The User Stories in the User Experiences(UX) part of this document is numbered 1 to 5. Below is a traceability matrix cross-referencing the user stories with the features, illustrating which features support which stories:

![UX Experience](documentation/ux/ux-image.png)

### Features which could be implemented in the future
- UI
It would be friendlier for the user if a user-interface layer was built using HTML/ CSS and possibly Javascript.

- Calculate monthly donations
It would be interesting for the user to see how many donations were made in a time frame. This would require a date stamp.

- User account
It would be useful for the user (and for the ficitional site) to encourage users to donate often and they can see what they have donated.

## Design

### Flow Chart
The diagram below outlines the flow of control within the application :

![Flow Chart](documentation/flow-chart/flow-chart.png)
## Technologies Used

### Languages Used

- [Python 3.11.4] (https://www.python.org/)

### Frameworks, Libraries & Programs Used

- [Google Speadsheets:](https://en.wikipedia.org/wiki/Google_Sheets) used as an external data store for the Events and Bookings data used by the project.
- [Google Drive API:](https://developers.google.com/drive/api/v3/about-sdk) used to generate credentials used in the project to securely access the Google Spreadsheet.
- [Google Sheets API:](https://developers.google.com/sheets/api) used to support interactions (e.g. read/write functionality) between the code and data stored in the Google Spreadsheet.
- [Google Auth:](https://google-auth.readthedocs.io/en/master/) Google authentication library for Python required to use the credentials generated for Google Drive API.
- [Miro:] (https://miro.com/) was used to create the flow chart.
- [Git:](https://gitscm.com/) was used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [GitHub:](https//github.com/) is used as the repository for the projects code after being pushed from Git.
- [Heroku:](https://heroku.com) is used to deploy the application and provides an environment in which the code can execute.

## Testing

### Validator Testing

- [Python Validator](https://pep8ci.herokuapp.com/)

- result for run.py

### Test Cases and Results

- The below table details the test cases that were used, the results and a cross-reference to the Feature ID that each test case exercised:

### Known Bugs

## Deployment

### How to clone the GitHub repository

### How to create and configure the Google speadsheet and APIs

### How this site was deployed to Heroku

## Credits

### Content

### Code

### Acknowledgements