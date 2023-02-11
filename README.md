# Purpose of this project

Blockchain technology is fascinating to me and I observe the emergence of numerous new applications that are accessible to users for testing purposes. This is known as a Testnet. It provides an opportunity for users to evaluate and provide feedback on the app's features. Once the project is ready for its mainnet release as a stable version, beta testers are usually rewarded with an airdrop.

![rewarded](static/assets/images/readme-images/diapo6.png)

Presently, we are witnessing a shift from web2 to web3, where in web2, all that was required for interaction with a platform was a login and password. With web3, users own a wallet, which serves as a means of interaction with blockchain platforms. This results in the management of various wallets and private keys.


![web2/web3](static/assets/images/readme-images/diapo5.png)



Analys of the main problem:

- Following all of the data that is required during a testnet can be somewhat complicated, as it often involves managing multiple pieces of information and keeping track of different accounts and logins. 
- When a beta tester becomes eligible to claim their reward, which can occur a year after their participation, they may find themselves in the following situation:

![Overloaded desktop](static/assets/images/readme-images/diapo7.png)

![Claim problem](static/assets/images/readme-images/diapo1.png)

During a Testnet, you may need to provide an email address to register for the testnet, and then use that email to confirm your registration and receive updates about the testnet. You may also need to create and manage a Discord account to join the testnet community, and use that account to communicate with other participants and receive instructions on how to claim your tokens. Similarly, you may be required to use a Telegram username or create a Github account to access certain features of the testnet.
It can be helpful to keep track of all the different pieces of information and account logins in a single place, this place is call Testnet Organizer and this is the app i will present here.


This project was developed in order to demonstrate 
some ability to :
- code in Python
- deal with boostrap 
- use Django

[Check this out](https://testnet-organizer.herokuapp.com/)

# Testnet Organizer

This application prioritizes bringing all information related to testnets into one central location. Registered users can create a section for a particular testnet, which displays all relevant information needed to participate. If another user decides to participate, they can duplicate the testnet section and make modifications with their own participation information. The aim is to create a dynamic within the app, where successful actions result in the accumulation of experience points, encouraging increased interaction with the app.

![mission board](static/assets/images/readme-images/diapo2.png)


# Contents

* [**User Experience UX**](<#user-experience-ux>)
    * [Wireframes](<#wireframes>)
    * [Structure of the app](<#structure-of-the-app>)
    * [Programming Structure](<#programming-structure>)
    * [Design Choices](<#design-choices>)
      -   [Typography](<#typography>)
      -   [Colour Scheme](<#colour-scheme>)
    * [User stories](<#user-stories>)
* [**Existing Features as a User**](<#existing-features-as-a-user>)
    * [Navigation](<#navigation>)
    * [Sign Up](<#sign-up>)
    * [Sign In](<#sign-in>)
    * [Sign Out](<#sign-out>)
    * [Edit Profile](<#edit-profile>)
    * [Add New Testnet](<#add-new-testnet>)
    * [Edit a Testnet](<#edit-a-testnet>)
    * [Copy a Testnet](<#copy-a-testnet>)
    * [Delete a Testnet](<#copy-a-testnet>)
    * [Users of the app](<#users-of-the-app>)
    * [Followers](<#followers>)
    * [Experience as a user](<#Experience-as-a-user>)
    * [Notification system](<#notification-system>)
    * [Report a Testnet](<#report-a-testnet>)
    * [Searching Users](<#searching-users>)
    * [Searching a testnet](<#searching-a-testnet>)
    * [Footer](<#footer>)


# User Experience (UX)

## Wireframes

I utilized [Balsamiq](https://balsamiq.com/learn/) to visually represent my ideas. From the outset, my goal was to design an efficient dashboard that presents all crucial information in an aesthetically pleasing manner.

Main focus was :
- Information about the user
- "all my Testnet" section
- Statistics about his participation within the app (followers, Testnet numbers etc)

![mission board](static/assets/images/readme-images/diapo3.png)

this is the final result of the dashboard :

![mission board](static/assets/images/readme-images/diapo4.png)


This is the organization of the differents interactions that a user will have with the app :

1 - HOME

![HOME](static/assets/images/readme-images/home.png)

2 - USERS PAGE

![USERS PAGE](static/assets/images/readme-images/userpage.png)

3 - DASHBOARD OF THE SELECTED USER

![DASHBOARD](static/assets/images/readme-images/dashboard1.png)

4 - COPYING TESTNET OF THIS USER

![COPY](static/assets/images/readme-images/copytestnet.png)

5 - YOUR DASHBOARD

![EDIT ON DASHBOARD](static/assets/images/readme-images/edit1.png)

6- EDIT A TESTNET

![EDIT TESTNET](static/assets/images/readme-images/edit2.png)

7 - YOUR DASHBOARD

![DASHBOARD SHOW](static/assets/images/readme-images/show1.png)

8 - SHOW YOUR TESTNET

![TESTNET SHOW](static/assets/images/readme-images/showtestnet.png)

9 - ADD A TESTNET

![TESTNET ADD](static/assets/images/readme-images/addtestnet.png)

10 - NOTIFICATIONS

![NOTIFICATIONS](static/assets/images/readme-images/notifications2.png)

![NOTIFICATIONS](static/assets/images/readme-images/notifications.png)

11 - FOLLOW A USER

![FOLLOW](static/assets/images/readme-images/follow1.png)

![FOLLOWED USER](static/assets/images/readme-images/follow2.png)


It's important to note that the final design may differ visually from the wireframes, due to design decisions made during the creation process.


[Back to top](<#contents>)

## Structure of the app

Testnet Organizer is divided in three components: 
- The authentication section, where users can register or log in to their existing account.
- The user section, where users can interact with Testnet(s), manage their personal information, Follow Users and Copy their Testnet. 
- The admin section, accessible to users with administrative privileges, which allows for the management of both users and Testnets (this section will be discussed in further detail later in the document).



To accomplish this, I had to develop a database table model to streamline the application's functionality. I used [Visual Studio Code](https://code.visualstudio.com/) to generate the following :

![TABLES](static/assets/images/readme-images/TABLE_TESTNET_ORGANIZER.png)

Throughout this project, I employed the principles of Object-Oriented Programming and utilized Django's Class-Based Views. For user authentication, I utilized Django AllAuth.

[Back to top](<#contents>)

Models used in this project are:

- **Testnet** : Handles Testnet with all the informations needed in both part, from the user who participate and the testnet itself.
- **UserInfo** : Handles User information, status (Admin, user, blocked user), avatar, bio etc...
- **Notifications** : Handles Users Notification tools. It allows to keep track on actions within the app, like following a new user, updating a Testnet, deleting a testnet but also more advances notifications like "A Testnet you copied have been updated, please check it out" or "One of the testnet you copied have been reported by a user, check it out"
- **User** : Handles basic information during the registering process, Username, email and password
- **Checklist** : Provides a checklist for the user to record specific information for the purpose of creating a testnet later on OR simply record a specific data to focus on.

The Model **Checklist** has been created in perspective on creating a new features later during a next update of the platform. This Model will not be used on the current version of the app (We talk about this later on in the document in "Future Features" section ).

[Back to top](<#contents>)

As you can see, every Testnet will have an Author and a Testnet User where :
- Author is the author of the Testnet
- Testnet User is the User who has copied the Testnet.

When a User create a Testnet it will be registered in the Testnet Table as Author and Testnet User.

[Back to top](<#contents>)


## Programming Structure

Before starting to code, I wanted to be confident with Django, so I've been starting reading the fantastic [Django Documentation](https://docs.djangoproject.com/en/4.1/) :

 **Before starting i wanted to be confident on** :
   - 1/ Authentification Module from Django 
   - 2/ Migrations from Models.py
   - 3/ Displaying the admin section with Custom Tables display
   - 4/ Interaction with Database
   - 5/ Dealing with boostrap Template
   - 6/ Deployment on Heroku 
   - 7/ Building own Class, specially for Forms
   - 8/ POST and GET request
   - 9/ Learning how to deal with Views
   - 10/ Dealing with pagination

[Back to top](<#contents>)


## Design Choices

 * ### Typography

	Honestly, I was fully cognizant of the level of functionalities I wanted for this app and how ambitious it was, thus my initial thought was to minimize the HTML and CSS coding, as those aspects had already been tackled in prior projects (Project 1 and 2).


Initially, I searched for an appropriate template on [Boostrap Website](https://startbootstrap.com/themes) and created a preliminary static version of the app to determine the placement of elements and to assess the feasibility of the design I created in Balsamiq.


I used this template as a basment : [Template Boostrap](https://startbootstrap.com/previews/sb-admin-angular) :


![TABLES](static/assets/images/readme-images/bootstrap.png)

And I created my first version of the app in static mode, only HTML and CSS :

![TABLES](static/assets/images/readme-images/versionstatic.png)

![TABLES](static/assets/images/readme-images/versionstatic2.png)

![TABLES](static/assets/images/readme-images/versionstatic3.png)

![TABLES](static/assets/images/readme-images/versionstatic4.png)


About the font : 

I have been experiencing some trouble to find the perfect font for my App. 
After trying Bebas_Neue, Delius, EB_Garamond and Playfair_Display, it's [Ubuntu](https://fonts.google.com/specimen/Ubuntu) that really attract me much. So, to have it locally and always available, I decided to download and call the font
from my style.css file :

![FONT](static/assets/images/readme-images/font1.png)

![FONT](static/assets/images/readme-images/font2.png)

 * ### Colour Scheme

With boostrap,I already had a pre-defined coloring panel to use :


![TABLES](static/assets/images/readme-images/panel.png)


- Success : green
- Primary : blue
- Secondary : grey
- danger : red
- warning : Yellow

So, when i need :
- a yellow button : btn-warning
- a blue text : text-primary
- or a red Text : text-danger

So Cool!

[Back to top](<#contents>)


### User stories

## User Stories


First Time Visitor Goals :
| Story | action required | Checked? |
|:-------:|:--------|:--------|
| As a first time visit | I want to understand the main purpose of the app | &check; |
| As a first time visit | I want to understand how to register and how to connect to the app | &check; |


The user stories for the project are listed below to clarify the significance of specific features.

### Site User
| Story | action required | Checked? |
|:-------:|:--------|:--------|
| As a Site User | I can access the home page, where I will discover the purpose of the application and the proposed solution to the specific problem. | &check; |
| As a Site User | I can Register as a new user of the App. If already registered, I can log in and log out | &check; |
| As a Site User | I can access to a Dashboard where I can find all my informations | &check; |
| As a Site User | I can change my profile information like avatar, bio etc... | &check; |
| As a Site User | I can display All the Testnet created by all the users of the app | &check; |
| As a Site User | I can see other Users of the app | &check; |
| As a Site User | I can follow and unfollow other users | &check; |
| As a Site User | I can display others dashboard with limited access | &check; |
| As a Site User | I can search for a specific user | &check; |
| As a Site User | I can search for a specific Testnet | &check; |
| As a Site User | I can see notifications when i realize an significant action within the app | &check; |

| As a Site User | I can see my experience within the app with nice basic statistics  | &check; |
| As a Site User | I can see the most active users of the app | &check; |
| As a Site User | I can Create, Edit and delete a Testnet of mine | &check; |
| As a Site User | I can Copy an existing Testnet from an other user | &check; |
| As a Site User | I can report a Testnet if I feel like some malicious links has been incorpored into a Testnet Informations | &check; |
| As a Site User | I will receive information as Notifications when a Testnet that I copied have been updated by the author so I can check it out what is updated| &check; |
| As a Site User | I can see the most popular Testnet of the App, which means the most copied Testnet by other users | &check; |
| As a Site User | I can Display the informations about any none Reported Testnet of the App | &check; |
| As a Site User | I can have an access to all my testnet(s) and I can see a different coloring design on each to get to know the difference between "Original", "Copied" or "Reported" | &check; |
| As a Site User | I can see an information box with the successful result of any significant actions within the app | &check; |

[Back to top](<#contents>)

### Site Admin

| Story | action required | Checked? |
|:-------:|:--------|:--------|
| As a Site Admin | I can log in and out | &check; |
| As a Site Admin | I can create, edit and delete a testnet of mine and from others | &check; |
| As a Site Admin | I can display all reported Testnet on the Testnet Board | &check; |
| As a Site Admin | I can cancel report on reported testnet and report none reported testnet | &check; |
| As a Site Admin | I can give admin role to a normal user  | &check; |
| As a Site Admin | I can block users and delete users | &check; |
| As a Site Admin | I can kick out a user from admin role | &check; |
| As a Site Admin | I can change my profile informations such as avatar, bio etc.. | &check; |
| As a Site Admin | I can have access to a admin board to manage Testnets and users of the app | &check; |
| As a Site Admin | I can receive specific notifications about a reported testnet | &check; |


The completion of each User Story is made clear through the defined acceptance criteria :
- Must have
- Should have
- Wont have

I used Github to manage the different user stories tasks :

![Agile](static/assets/images/readme-images/Agile.png)

This is the final status of the Agile Strategy displayed:

![Agile](static/assets/images/readme-images/agile2.png)


[Back to top](<#contents>)

# Existing Features as a User

## Navigation

When discovering the app for very first time, you have access to home page which is a dedicated page for user to understand the purpose of the app.


![barnav](static/assets/images/readme-images/purposeapp.png)

Also, User can see some stats about the App, Numbers of active users and Numbers of registered Testnet on the App.

![barnav](static/assets/images/readme-images/statsapp.png)


 Then, you can access to "login" button or a "Register" button :

![barnav](static/assets/images/readme-images/barnav1.png)

If User click on Register button, User will have access to a registration Form  :

![registration form](static/assets/images/readme-images/register.png)

If User click on Connect button, User will have access to a Connection Form  :

![Connection form](static/assets/images/readme-images/connection.png)


When a user is logged in, they have access to the following resources:

- Users: The user can view all users of the app and perform a search for a specific user.
- Testnets: The user can view all testnets of the app, including their own testnets and those of other users. They also have the ability to search for a specific testnet.
- Dashboard: The user has access to all information related to their account, including their stats and experience points within the app, notifications, profile information, and a list of their latest published testnets.
- Logout : This button allow to a connected User to log out from the app.

![Bar Nav when connected](static/assets/images/readme-images/barnavconnecte.png)



[Back to top](<#contents>)


## Sign Up

When a User decide to Register to the app, it will happen the following :
- If Registration form is correctly filled then :
  * Auto-Redirection to Dashboard.
  * Creation of the user into UserInfo Table with basic pre-registered info, pre-selected avatar and pre-written bio. (User can edit anytime)


![Profile created with basic info](static/assets/images/readme-images/pre_registered_profile.png)

Then a fresh Dashboard will appear :

![New Dashboard](static/assets/images/readme-images/new_dashboard.png)


[Back to top](<#contents>)


## Sign In

When a User enter the App with a existing username and correct password, it will happen the following :

- A message indicate User is successfully connected. The NavBar appear with full possibilities :  Dashboard, Testnet, Users

![Enter to the app](static/assets/images/readme-images/connection_successful.png)


[Back to top](<#contents>)


## Sign Out

When a User click on Logout button, a prompt message will appear :

![Sign out](static/assets/images/readme-images/sure_sign_out.png)

If User click on Sign Out button again, then User will be logged out from the app and a message will be displayed :

![message Sign out](static/assets/images/readme-images/signout_message.png)

## Edit Profile

User can Edit Profile anytime and as many time as User want.

For that, click on the button "Edit profile" :

![Edit Profile](static/assets/images/readme-images/edit_profile.png)

A form will appears :

![Edit Profile](static/assets/images/readme-images/profile_edit_form.png)

Here User can edit, Bio, Debank adresse, Avatar picture.

Username of the User cannot be modified!

Profile will be updated if User modify something, and a message will be displayed :

![Updated Profile](static/assets/images/readme-images/updated_profile_message.png)


![Updated Profile](static/assets/images/readme-images/profile_updated.png)

[Back to top](<#contents>)

## Add New Testnet

Once Registered or Logged, a User can Create a new Testnet :

A button is displayed to realize this action :
- on Dashboard

![Add new testnet](static/assets/images/readme-images/from_dashboard.png)

- on Testnet Page

![Add new testnet](static/assets/images/readme-images/from_testnet_page.png)

A form is displayed :

![Add new testnet](static/assets/images/readme-images/form_new_testnet1.png)

![Add new testnet](static/assets/images/readme-images/form_new_testnet2.png)

![Add new testnet](static/assets/images/readme-images/form_new_testnet3.png)

![Add new testnet](static/assets/images/readme-images/form_new_testnet4.png)

If the form is correctly filled, a message will appears:

![Add new testnet message](static/assets/images/readme-images/testnet_message.png)

And the Testnet will appears as the last Testnet created on Dashboard :

![Add new testnet](static/assets/images/readme-images/testnet_message.png)

required inputs during the creation of a New Testnet :

* Testnet name
* Testnet Network
* Testnet Description
* Testnet Status
* Testnet Category
* Testnet Tasks Description

Of course, Testnet name should be unique on the plateform and if User type an existing Testnet, it will display 
the following message : 

![Add new testnet already exist](static/assets/images/readme-images/already_exist.png)


If the creation of a new Testnet is successfull, the User will receive a Notification :

![Add new testnet success](static/assets/images/readme-images/addtestnetnotification.png)


[Back to top](<#contents>)


## Edit a Testnet

There are several places you can start editing a Testnet that belong to the connected User :

- From the section "ALl New Testnet" :

![Add new testnet](static/assets/images/readme-images/edit from testnet new.png)

- From the section "All My Testnet" :

![Add new testnet](static/assets/images/readme-images/edit from all your testnet.png)

- From the displayed Testnet itself :

![Add new testnet](static/assets/images/readme-images/edit from testnet itself.png)


When editing a Testnet there are two differents displayed Form :

- When your Testnet is a copy

![Editing copy Testnet](static/assets/images/readme-images/copytestnet1.png)

![Editing copy Testnet](static/assets/images/readme-images/copytestnet2.png)

![Editing copy Testnet](static/assets/images/readme-images/copytestnet3.png)

As you can see, only inputs related to Users experience with this Testnet is available for editing.
All the Grey inputs are data from the Original Testnet author and will be updated if the Author realized an edition on it.



- When your Testnet is an Original and User is the author



![Editing copy Testnet](static/assets/images/readme-images/editing when author.png)

As you can see, all inputs are available to edition. 

Consequences :

* If an User update an Original Testnet and User is the Author, All users that copied this Testnet will receive a Notification about this update and
also, all updates/modifications will appears on the copied Testnet.

Cool, right!

After submitting the changes of an Original Testnet and User connected is the Author, User will see the following message :

![Editing copy Testnet message](static/assets/images/readme-images/success_edition_testnet.png)

If updated Testnet is a Copy, User will see the following message :

![Editing copy Testnet message](static/assets/images/readme-images/success_edition_testnet2.png)


[Back to top](<#contents>)


## Copy a Testnet

When a User find a Testnet to participate, User can choose to **Copy** this Testnet to add it own data as :
- Testnet Name
- All info about the account used to participate as Discord account, Telegram account, Twitter account etc..
- All info about the wallet used to participate as Wallet adress, password, seed phrase etc..
- All info about the User participation as Transaction links, data , snapshots, email content etc..

All thoses data are only displayed for the User, in any case other Users can see thoses informations.

User can also Copy an already Copied Testnet so it allow User to participate to same Testnet but with 
different account informations. When participation is double, the rewards are double also :-D

When a User click on the copy button, a prompt message is displayed :

![Copy Testnet](static/assets/images/readme-images/copytestnetinfo.png)

If accepted, User will have access to a Form where User can edit the copy of this Testnet with information in relation to 
his participation.

If the copied Testnet is a copy from his own Original, User will see the following message on Notifications :

![Copy Testnet](static/assets/images/readme-images/duplicatetestnet.png)


If the User copy an Original Testnet but not the Author, User will see the following message on Notifications :

![Copy Testnet](static/assets/images/readme-images/duplicatetestnet2.png)


[Back to top](<#contents>)


## Delete a Testnet

* If Connected User is the owner of a Copied Testnet, User can delete it at any time :

![Delete Testnet](static/assets/images/readme-images/deletetestnet.png)


A prompt message is displayed to confirm the fact of deleting this current Testnet :

![Delete Testnet](static/assets/images/readme-images/deletetestnet1.png)


if User decide to proceed to delete this Testnet, it will display the following message :

![Delete Testnet](static/assets/images/readme-images/deletetestnetmessage.png)


And User will get a Notification :

![Delete Testnet](static/assets/images/readme-images/notificationdeletedTestnet.png)



* If the User who is connected is the creator of the Testnet, all users who have replicated this testnet will receive a notification containing the information they provided when they made their copy.

![Delete Testnet](static/assets/images/readme-images/deletedbyauthor.png)


and the following message will be displayed :

![Delete Testnet](static/assets/images/readme-images/deletedbyauthor2.png)

[Back to top](<#contents>)


## Users of the app

Connected User can access to the "Users" section to get the 12 most active players of this app.

![users](static/assets/images/readme-images/mostactiveusers.png)


on this page, User can follow, unfollow a User , search a User or display other User Dashboard with limited information(s)

This is an example of User Dashboard that any user of the app can access :

![Users](static/assets/images/readme-images/displayuserdashboard.png)

[Back to top](<#contents>)

## Followers

This User section can allow any connected user to follow to each other. By clicking on the empty star icon, you can follow a User. 

![follow user](static/assets/images/readme-images/users1.png)

When user click on the empty stars, a prompt message will be displayed :

![follow user](static/assets/images/readme-images/users2.png)

when confirmed, a notification will be send to the user that follow but also the followed user :

![follow user](static/assets/images/readme-images/users5.png)

![follow user](static/assets/images/readme-images/users6.png)


And a message will be displayed on the screen :

![follow user](static/assets/images/readme-images/users3.png)

when user display again users, a followed user must be displayed with a full star icon as following :

![follow user](static/assets/images/readme-images/users4.png)

[Back to top](<#contents>)

## Experience as a user

As a User, every significant actions as :
* Create a Testnet 
* Get followed by an other
* Get A created Testnet copied by an other user 

makes the User earning Experience on the app.

For a User to get Level up, User need to accomplish all the Tasks.

AS you can see, each level get a certain amount of Followers to have, Created Testnet and Testnet Copied from others.

![stats user](static/assets/images/readme-images/statsusermission.png)

Of course, If a user get unfollowed by an other user or delete one of the created Testnet it will decrease the total
amount of EXP. The same situation happen if a User delete a Testnet (not copies)

![manage user experience](static/assets/images/readme-images/manageexp.png)

[Back to top](<#contents>)

## Notification system

Every Users of the App have a Notification board where it's displayed all the actions realized by the user.

![notifications](static/assets/images/readme-images/seenotif.png)


If User click on "Show", User can see Unread notification(s) and Read notification(s) :

Read Notification(s) :

![notifications](static/assets/images/readme-images/read.png)

Unread Notification(s) :

![notifications](static/assets/images/readme-images/unread.png)

When User click on the button "OK" on unread notification(s) it will transfer the notification to "Read Notification" section :

![notifications](static/assets/images/readme-images/clicknotif.png)

![notifications](static/assets/images/readme-images/notiftransfered.png)

[Back to top](<#contents>)

## Report a Testnet

It's important to ensure the security of our platform by verifying that all links entered by users are legitimate. This is crucial because allowing a malicious link can result in a phishing attack scam.

How to protect the App from it?

It's simple, as long as a Testnet contains suspicious on having malicious links, any users can report it and it will be blocked directly from copying and editing.
A red message will be displayed to inform all users about this Testnet.

![report testnet](static/assets/images/readme-images/reportedtestnet.png)

![report testnet](static/assets/images/readme-images/reportedtestnet1.png)

![report testnet](static/assets/images/readme-images/reportedtestnet2.png)

User who made the report will receive a notification :

![report testnet](static/assets/images/readme-images/reportedtestnet3.png)

And all Users with administration role will receive a notification as following :

![report testnet](static/assets/images/readme-images/reportedtestnet4.png)

In case one of the Connected User's Testnet has been reported, User will be informed with notification :

![report testnet](static/assets/images/readme-images/reportedtestnet5.png)

In this documentation, we will cover later how users with administrative roles handle reported Testnet issues.


[Back to top](<#contents>)

## Searching Users

As a user, it's possible to search any unblocked User of the App by typing at least 3 characters on the search input :

![search user](static/assets/images/readme-images/searchingusers.png)

If user only provide less than 3 character, it will appears the following messages :

![search user](static/assets/images/readme-images/searchingusers1.png)


If the search input is filled correctly :

![search user](static/assets/images/readme-images/searchingusers2.png)

Users can still access the same features, including the ability to view the dashboard of a searched user and follow or unfollow them.

[Back to top](<#contents>)

## Searching a testnet

There are several way to reach the Testnet research's section :

On dashboard :

![Searching Testnet](static/assets/images/readme-images/searchtestnet1.png)


On All New Testnet Section :

![Searching Testnet](static/assets/images/readme-images/searchtestnet2.png)
 
On all testnet from selected user's section :

![Searching Testnet](static/assets/images/readme-images/searchtestnet3.png)

If result of the research show more than 8 results, a pagination system is deployed :

![Searching Testnet](static/assets/images/readme-images/searchtestnet4.png)

The research function will search into:
* Testnet names
* Testnet's description
* Username

![Searching Testnet](static/assets/images/readme-images/searchtestnet5.png)

[Back to top](<#contents>)

## Footer

A footer is always displayed on the bottom of the App :

![Footer](static/assets/images/readme-images/footer.png)