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
* [**Existing Features as an admin**](<#existing-features-as-a-admin>)
    * [Navigation](<#navigation>)
    * [Same features as a normal user](<#same-features-as-a-normal-user>)
    * [Reported Testnet](<#reported-testnet>)
    * [Board Users](<#board-users>)
* [**Future Features of the app**](<#future-features-of-the-app>)
    * [A Forum](<#a-forum>)
    * [Notification tools for admin](<#notification-tools-for-admin>)
    * [Check List](<#check-list>)
    * [Trust score recording](<#trust-score-recording>)
    * [Testnet notations](<#testnet-notations>)
* [**Technologies**](<#technologies>)
    * [Languages](<#languages>)
    * [Frameworks and Software](<#frameworks-and-software>)
    * [Libraries](<#libraries>)
    * [Tools](<#tools>)
* [**Testing**](<#testing>)    
    * [User Story Testing](#user-story-testing)
    * [Validator HTML CSS PYTHON](#validator-html-css-python)
      * [HTML](#html)
      * [CSS](#css)
      * [Python](#python)
    * [Lighthouse](#lighthouse)
    * [Browser Testing](#browser-testing)
    * [Device Testing](#device-testing)
    * [Manual Testing](#manual-testing)
      * [Site Navigation](#site-navigation)
      * [Browse Page](#browse-page)
      * [Add Testnet](#add-testnet)
      * [Update Testnet](#update-testnet)
      * [Prompt Message before significant action](#prompt-message-before-significant-action)
      * [Admin Board](#admin-board)
      * [Avoid actions from URL](#avoid-actions-from-url)
    * [Form Validation](#form-validation)
    * [error pages](#error-pages)



    

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

I've been having difficulty finding the ideal font for my app. I tried Bebas Neue, Delius, EB Garamond, and Playfair Display, but [Ubuntu](https://fonts.google.com/specimen/Ubuntu) font caught my attention the most. To have it readily accessible, I opted to download it and reference it in my style.css file directly :

![FONT](static/assets/images/readme-images/font1.png)

![FONT](static/assets/images/readme-images/font2.png)

 * ### Colour Scheme

With boostrap, I already had a pre-defined coloring panel to use :


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
| As a first time visit | I want to see a Welcome message | &check; |


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

When discovering the app for very first time, a User have access to home page which is a dedicated page for user to understand the purpose of the app.


![barnav](static/assets/images/readme-images/purposeapp.png)

Also, User can see some stats about the App, Numbers of active users and Numbers of registered Testnet on the App.

![barnav](static/assets/images/readme-images/statsapp.png)


 Then, you can access to "login" button or a "Register" button :

![barnav](static/assets/images/readme-images/barnav1.png)

If User click on Register button, User will have access to a registration Form  :

![registration form](static/assets/images/readme-images/register.png)



If User click on Connect button, User will have access to a Connection Form  :

![Connection form](static/assets/images/readme-images/connection.png)


When a user is logged in, User have access to the following resources:

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
  * A Welcome Message is displayed
  * A notification are sent to the User about this event
  * Creation of the user into UserInfo Table with basic pre-registered info, pre-selected avatar and pre-written bio. (User can edit anytime)


![Profile created with basic info](static/assets/images/readme-images/pre_registered_profile.png)

When registered, User will see a Welcome Message and a Notification :

![Welcome Message](static/assets/images/readme-images/welcome.png)

![Welcome Message](static/assets/images/readme-images/welcome1.png)


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

User can Edit Profile anytime and as many time as User wants.

For that, click on the button "Edit profile" :

![Edit Profile](static/assets/images/readme-images/edit_profile.png)

A form will appears :

![Edit Profile](static/assets/images/readme-images/profile_edit_form.png)

Here User can edit Bio, Debank adresse, Avatar picture.

[Back to top](<#contents>)

**Username of the User cannot be modified!**

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

![Add new testnet](static/assets/images/readme-images/lasttestnet.png)

[Back to top](<#contents>)

Required inputs during the creation of a New Testnet :

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

There are several places a Connected User can start editing a Testnet that belong to him:

- From the section "All New Testnet" :

  ![Add new testnet](static/assets/images/readme-images/editfromtestnetnew.png)

- From the section "All My Testnet" :

![Add new testnet](static/assets/images/readme-images/editfromallyourtestnet.png)

- From the displayed Testnet itself :

![Add new testnet](static/assets/images/readme-images/editfromtestnetitself.png)

[Back to top](<#contents>)

When editing a Testnet there are two differents displayed Form :

- When your Testnet is a copy

![Editing copy Testnet](static/assets/images/readme-images/copytestnet1.png)

![Editing copy Testnet](static/assets/images/readme-images/copytestnet2.png)

![Editing copy Testnet](static/assets/images/readme-images/copytestnet3.png)

As you can see, only inputs related to Users experience with this Testnet is available for editing.
All the Grey inputs are data from the Original Testnet author and will be updated if the Author realized an edition on it.



- When your Testnet is an Original and User is the author


![Editing copy Testnet](static/assets/images/readme-images/editingwhenauthor.png)

As you can see, all inputs are available to edition. 

Consequences :

* If an User update an Original Testnet and User is the Author, All users who copied this Testnet will receive a Notification about this update and
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


If the User copy an Original Testnet but Current logged User is not the Author, User will see the following message on Notifications :

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

Connected User can access to the "Users" section to get the 20 most active players of this app.

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

when confirmed, a notification will be send to the fuser that follow but also the followed user :

![follow user](static/assets/images/readme-images/users5.png)

![follow user](static/assets/images/readme-images/users6.png)

Note : The followed User will receive Exp points for this.
Of course, if the user decide to Unfollow, the followed User will loose some EXP points.


And a message will be displayed on the screen :


![unfollow user](static/assets/images/readme-images/unfollowuser1.png)

![follow user](static/assets/images/readme-images/users3.png)

when user display again "users" section, a followed user must be displayed with a full star icon as following :

![follow user](static/assets/images/readme-images/users4.png)

But, We could naturally ask :
What is the point to follow Users ?
That's a good question, actually, following a User will give you an Notifications when one of your followed User
have created a New Testnet.

![follow user](static/assets/images/readme-images/notifwhenfollowing.png)


[Back to top](<#contents>)

## Experience as a user

As a User, every significant actions as :
* Create a Testnet 
* Get followed by an other
* Get A created Testnet copied by an other user 

makes the User earning Experience on the app.

For a User to get Level up, User need to accomplish all the displayed Tasks on dashboard mission section.

As you can see, each level get a certain amount of Followers to have, Created Testnet and Testnet Copied from others.

![stats user](static/assets/images/readme-images/statsusermission.png)

Of course, If a user get unfollowed by an other user it will decrease the total
amount of EXP of the user. The same situation happen if a User delete a Testnet (not copies)

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

It's simple, as long as a Testnet contains suspicious malicious links, any users can report it and it will be blocked directly from copying and editing.
A red message will be displayed to inform all users about this Testnet.


From a testnet information itself :

![report testnet](static/assets/images/readme-images/reportbuttonfortestnet.png)

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

If user only provide less than 3 characters, it will appears the following messages :

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

If result of the research show more than 8 results, a pagination system is deployed automatically :

![Searching Testnet](static/assets/images/readme-images/searchtestnet4.png)

The research function will search into:
* Testnet names
* Testnet's description
* Testnet User

![Searching Testnet](static/assets/images/readme-images/searchtestnet5.png)

[Back to top](<#contents>)

## Footer

A footer is always displayed on the bottom of the App with blank target for each links to ensure User never goes away from the app :

![Footer](static/assets/images/readme-images/footer.png)

[Back to top](<#contents>)

# Existing Features as an admin

## Navigation

The navigation as an admin is exactly the same as a normal user. 
With administration role, a User can access to two new sections :
- Board Users
- Board Testnet

![Admin Section](static/assets/images/readme-images/adminsection1.png)

[Back to top](<#contents>)

## Same features as a normal user

With Administration Role an Admin can access to the same functionalities as a normal User for :
- Creating Testnet
- Editing Testnet
- Copy a Testnet from an other User
- Edit Profile
- Follow/Unfollow other users
- Get experience from interacting with the app
- Report a Testnet

At the end, an admin is an normal User with some special privileges in order to administrate Testnets and Users of the App.

[Back to top](<#contents>)

## Reported Testnet

In the "Board Testnet" section, an admin can do several things :

- Search any testnet from the App
- See all Reported Testnet(s) { 1 }
- See if a Testnet is a copy { 4 } or an Original  { 2 }
- Report a Testnet { 3 } 
- Cancel report to a Testnet { 5 } 
- Display the Testnet { 6 } 
- In case the current admin is the author, report is disabled { 7 } 

![Admin Section](static/assets/images/readme-images/admintestnet1.png)

If admin click on "Cancel Report", the following promtp is displayed :

![Admin Section](static/assets/images/readme-images/admintestnet2.png)


In case, Admin click on "Report", the following prompt is displayed :

![Admin Section](static/assets/images/readme-images/admintestnet3.png)


In case, Admin click on "View", the Testnet will be displayed as the following :

A message will indicate that this Testnet is Reported. Copy and edition is not available.

![Admin Section](static/assets/images/readme-images/admintestnet4.png)

Admin can cancel the report from here by clicking on "Cancel Report".

Note that, On previous picture, it seems the Testnet has no data to show but it's because only the required
inputs have been filled (Testnet name, network, status, tasks description, Category).
Of course, if user register all the information, everything will appears like this :

![Board admin section](static/assets/images/readme-images/showtestnetwhenfilled.png)


[Back to top](<#contents>)

## Board Users

![Board Users Section](static/assets/images/readme-images/admintestnet5.png)

As you can see, this administration board for users give the user with admin role the possibility to :

* See all the blocked User {1} :
  This button allow the Admin to have all blocked Users of the App. 
  If the amount of blocked user is more than 8, a pagination will be automatically deployed :

[Back to top](<#contents>)

![Deleted User](static/assets/images/readme-images/paginationblockeduser.png)
  

* Delete a User from the App {2} :
  The Admin can permanently remove a user from the app using the "Delete" button. This will result in the deletion of all testnets and copies of the user from the app, and a notification will be sent to all users who have copied testnets from this user. However, before the "Delete" button becomes available, the Admin must first block the user. This added layer of protection helps prevent accidental deletions. Blocking a user temporarily hides their presence on the app, as well as their testnets and dashboard, from other users, giving the Admins time to discuss and make a final decision on the user's status.

Before Deleting User, a prompt will be displayed : 

![Deleted User](static/assets/images/readme-images/deletinguser.png)


 A message is displayed :

![Deleted User](static/assets/images/readme-images/deletedusermessage.png)
 

 An a notification is sent To admin :

![Deleted User](static/assets/images/readme-images/notifdeleteduser.png)
 

 All User who copied one of this deleted User Testnet will receive this following Notification :

![Deleted User](static/assets/images/readme-images/deletedusersodeletedcopitestnet.png)

[Back to top](<#contents>)

* Unblock a User {3} :

An admin can unblock a user who have been blocked previously.

If a blocked User try to log in, User will see the following page : 

![unblock User](static/assets/images/readme-images/unblockuser4.png)


This is the only thing a blocked user can see, nothing else, not even the dashboard. User interaction within the App
is reduce to 0.

If an admin click on "Unblock", a prompt message is displayed :

![unblock User](static/assets/images/readme-images/unblockuser3.png)


If accepted, admin will see a message :

![unblock User](static/assets/images/readme-images/unblockuser2.png)


And a notification is sent :

![unblock User](static/assets/images/readme-images/unblockuser1.png)


An unblocked user will regain immediate access to the platform. Welcome Back! :-D

[Back to top](<#contents>)

* View a User {4} :

This button will directly reach the user dashboard.
If the user is already blocked, the dashboard will be displayed as following :

![view](static/assets/images/readme-images/blockeddashboard.png)


[Back to top](<#contents>)

* Give Admin role to a User {5} :

If a User is not blocked, An Admin can give him the Admin role.

A prompt message is displayed :

![Admin Role](static/assets/images/readme-images/adminrole1.png)


If accepted, a message is displayed :

![Admin Role](static/assets/images/readme-images/adminrole5.png)


and a notification is sent to both admin and the New Admin user :

![Admin Role](static/assets/images/readme-images/adminrole2.png)

![Admin Role](static/assets/images/readme-images/adminrole3.png)


An Admin can be kicked out from the adminitration role at any time by clicking on this following button :

![Admin Role](static/assets/images/readme-images/adminrole6.png)


I developped a coloring tools to see directly which user is Active, Blocked, Admin :

![Admin Role](static/assets/images/readme-images/adminrole7.png)


[Back to top](<#contents>)


* Block a User {6} :

An admin can block a User from the App.

If a blocked User try to log in, it will see the following page : 

![Unblocked user](static/assets/images/readme-images/unblockuser4.png)


This is the only thing a blocked user can see, nothing else, not even the dashboard. User interaction within the App
is reduce to 0.

Note: If an Admin clicks the "Block" button on another Admin user, that user will lose their admin privileges and become a regular, blocked user. To regain their admin status, they will need to be reinstated as an Admin by another Admin

[Back to top](<#contents>)

# Future Features of the app
  ## A Forum
  Having a dedicated space for users to discuss Testnets would be amazing. Users who encounter challenges completing tasks could request assistance by sharing screenshots to highlight the issue. Upon receiving a satisfactory solution, they could be rewarded with bonus experience points.

  ## Notification tools for admin
  Notifications can be an incredibly useful tool for administrators to send a message to everyone in the app simultaneously. For instance, if a reward claiming event is underway, the administrator can make an announcement directly through the app, and all users will know that the notification came from an administrator and is legitimate. Having a Notification Management section for administrators would be convenient for them to communicate with everyone in the app.

  ## Check List
  Sometimes, you may come across information about a Testnet that you want to participate in, but it's not the right moment to start. I suggest creating a simple checklist, similar to taking notes, where a user can quickly jot down information about the Testnet without actually creating it within the app. When the user has more time, they can use this checklist to create the Testnet. The checklist would be positioned at the top of the "Create Testnet" form for easy copy-paste functionality.


  ## Trust score recording
  It would be beneficial to maintain a trust score for all users. For example, if a user has a Testnet deleted by an administrator due to a report, their trust score should decrease, indicating to other users that this individual may not be completely trustworthy in terms of copying their Testnets. On the other hand, if a user creates many Testnets and none of them have ever been deleted by an administrator, they can be considered to have a 100% trust score.

  ## Testnet notations
  To provide a clearer indication of the level of difficulty of a Testnet, users could rate it on a scale of 1 to 5. This way, whether a user is a beginner or an expert, they will be able to determine if a Testnet is too challenging for their skill level. The actual difficulty score would be determined by the average of all users' ratings for each Testnet.



# Technologies

## Languages

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) - Provides the functionality for the site.
* [CSS](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
* [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.

## Frameworks and Software


- [Django](https://www.djangoproject.com/) python framework used in the development of this App
- [Django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): authentication library used to create users accounts
- [PostgreSQL](https://www.postgresql.org/) Hosting database for this App
- [Heroku](https://dashboard.heroku.com/login) for deployment of the App.
- [Balsamiq](https://balsamiq.com/) to generate Wireframe of the App.
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) to test responsiveness and performance.
- [Font Awesome](https://fontawesome.com/) for icons of the App.
- [GitHub](https://github.com/) to manage agile tool and Hosting of the Code of this App.
- [Google Fonts](https://fonts.google.com/) to select the perfect font for my App.
- [PEP8 Validation](http://pep8online.com/) to Python code Validation
- [Favicon](https://favicon.io/) to create favicon.
- [Cloudinary](https://cloudinary.com/) to host images of the App , especially Avatar images from all users
- [Bootstrap](https://getbootstrap.com/docs/4.6/getting-started/introduction/) to responsiveness and styling of the App, Thanks Bootstrap Team !
- [CSS Validation](https://jigsaw.w3.org/css-validator/) to validate CSS code validation
- [HTML Validation](https://validator.w3.org/) to validate HTML code validation
- [VSCode](https://code.visualstudio.com/) to create the Models Graph of the app
- [a11y Color Contrast Accessibility Validator](https://color.a11y.com/Contrast/) to test color contrast on the App
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)to test performance of the App.
- [GitBash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)) - Terminal in [Gitpod](https://www.gitpod.io) to push commits to GitHub.


[Back to top](<#table-of-content>)


## Libraries

The following libraries are located in the requirements.txt file from the App:

* [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python
* [cloudinary](https://pypi.org/project/cloudinary/) - Manage Cloud images Items
* [dj3-cloudinary-storage 0.0.6](https://pypi.org/project/dj3-cloudinary-storage/) - Django package for Cloudinary by implementing Django Storage API.
* [Django](https://pypi.org/project/Django/) - Python web framework.
* [django-allauth](https://pypi.org/project/django-allauth/) - Allows authentication, registration and account management .
* [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - Used to integrate Django forms in the App.
* [django-extensions](https://pypi.org/project/django-extensions/) - Custom extensions for Django Framework.
* [gunicorn](https://pypi.org/project/gunicorn/) - Gunicorn is a Python HTTP Server.
* [oauthlib](https://pypi.org/project/oauthlib/) - Framework which implements OAuth1 or OAuth2.
* [psycopg2](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for Python.
* [PyJWT](https://pypi.org/project/PyJWT/) - A Python implementation.
* [python3-openid](https://pypi.org/project/python3-openid/) - OpenID support and features.
* [pytz](https://pypi.org/project/pytz/) - Python packages.
* [requests-oauhlib](https://pypi.org/project/requests-oauthlib/) - OAuth library support.
* [sqlparse](https://pypi.org/project/sqlparse/) - non-validating SQL parser for Python.


[Back to top](<#table-of-content>)


## Tools

Two fantastic tools for developpers :

* Shell_Plus : 

This tool is powerful, it pre-import all the dependencies you will need to interact with Tables :

![Tools](static/assets/images/readme-images/shell-plus1.png)

Once imported, you can execute request to the table and see the direct result.

![Tools](static/assets/images/readme-images/shell-plus2.png)

It helps me a lot when it's about write more complex request with cross-tables requests.

* Breakpoint() : 

Breakpoint allow you to place a break to your code and execute some code on the shell to see the
status of variables. It can be helpful to detect some stupid coding mistakes...

![breakpoint](static/assets/images/readme-images/breakpoint1.png)

![breakpoint](static/assets/images/readme-images/breakpoint2.png)

![breakpoint](static/assets/images/readme-images/breakpoint3.png)

[Back to top](<#table-of-content>)

# Testing

  ## User Story Testing

  **First Time visit** :

  * As a first time visit I want to understand the main purpose of the app

  When User visit the App for first time, User will have access to the index.html page :

  ![user stories test](static/assets/images/readme-images/userstories1.png)

  ![user stories test](static/assets/images/readme-images/userstories2.png)

  The purpose of this content is to clarify the function of the app.


  * As a first time visit  I want to understand how to register and how to connect to the app 

  When User visit the App for first time, User will have access to the following buttons:

  ![user stories test](static/assets/images/readme-images/userstories3.png)

  ![user stories test](static/assets/images/readme-images/userstories4.png)

  The only way to proceed further is by interacting with those buttons.

  *  As a first time visit  I want to see a Welcome message

  As long as a User have registered to the App, it will displayed the following :

  A message :

  ![user stories test](static/assets/images/readme-images/userstories5.png)

  A notification :

  ![user stories test](static/assets/images/readme-images/userstories6.png)

  [Back to top](<#table-of-content>)


  **As a User** :

  * As a Site User  I can Register as a new user of the App. If already registered, I can log in and log out 

  As a user, you can register to the App giving a username (should be unique) and password, email is optional.

  As a user, you can log in to the app with the given username and password you enter when registration process.

  *  As a Site User  I can access to a Dashboard where I can find all my informations 

  As a Connected User, you have access to a Dashboard where a User can find :
    - Profile
    - Experience on the App
    - Mission to accomplish to level up
    - 8 Last Testnet Registered (Click "Show More" to see all of them and make a search)
    - The very Last created Testnet
    - Followers number
    - Following Number
    - Testnet Number
    - Notification Number and a button to display them all

  *  As a Site User  I can change my profile information like avatar, bio etc...   

  As a Connected user, you can edit your profile as many as you want :

  - Description of yourself
  - Debank adress for others Users to follow you on debank also
  - Avatar

  The only thing that a User cannot change is the Username. 
  For now, the user cannot change his password either but this functionality will be available in a further update of the app as it was not a "Must have" features from the Agile Methodology.

  * As a Site User  I can display All the Testnet created by all the users of the app 
  
  As a connected User, you can see all your testnet but also all the Testnet from other Users. There is no option for having a private Testnet on the App. As long as you created a Testnet , it's published. Of course, A testnet can be reported and become no longer available for publishing.
  There is also the possibility for a Connected User to search any keyword on the search form:

  ![user stories test](static/assets/images/readme-images/userstories7.png)


  *  As a Site User  I can see other Users of the app

  As a connected user, you have access to the "Users" section where you can see :

  - the 20 Most active Users of the App
  - A search button is available to seek a specific user

  ![user stories test](static/assets/images/readme-images/userstories8.png)

  *  As a Site User  I can follow and unfollow other users   

  As a connected User, you can follow and Unfollow other user. If You follow an other user, it will allow you to :

  - Receive a notification when this followed user create a new Testnet.

  ![user stories test](static/assets/images/readme-images/userstories9.png)

  * As a Site User  I can display others dashboard with limited access   

  As a connected User, After following a User, you will have access to his dashboard with limited informations displayed :

  ![user stories test](static/assets/images/readme-images/userstories10.png)

  As we can see, only limited information(s) are displayed on Other User's Dashboard.

  As a connected User, you can have access to other User's Dashboard from "Users" section also.

  ![user stories test](static/assets/images/readme-images/userstories11.png)

  *  As a Site User  I can search for a specific Testnet   

  As a connected User, you can use the search button to seek a specific key word for a Testnet.

  ![user stories test](static/assets/images/readme-images/userstories12.png)

  The App will look into :
  - Testnet Name
  - Testnet Description
  - Testnet Username

  * As a Site User  I can see notifications when i realize an significant action within the app  

  As a connected User, we can access to notification section where all significant action's results are displayed:

  ![user stories test](static/assets/images/readme-images/userstories13.png)

  Of course, some notifications are displayed with links to direct access as :
  
  - A testnet
  - A user

  * As a Site User  I can see my experience within the app with nice basic statistics   

  Yes you can! As a Connected user, you have access to your experience Board where is displayed :

  - Your Exp on the App
  - Your Tasks status
  - Your Level on the App

 ![user stories test](static/assets/images/readme-images/userstories14.png)

 * As a Site User  I can Create, Edit and delete a Testnet of mine 

 As a connected User, you can :
 - Create a new Testnet
 - Edit an existing Testnet of yours
 - Delete a Testnet of yours

  ![user stories test](static/assets/images/readme-images/userstories15.png)

  ![user stories test](static/assets/images/readme-images/userstories16.png)

* As a Site User  I can Copy an existing Testnet from an other user   

As a connected User, I can Copy an existing Testnet from other Users. You can even copy an existing Testnet of yours. In fact, You can decide to participate to same Testnet but with different email account or Discord account. 
All published Testnet are available for copy except when a Testnet is Reported.

![user stories test](static/assets/images/readme-images/userstories17.png)

![user stories test](static/assets/images/readme-images/userstories18.png)

* As a Site User  I can report a Testnet if I feel like some malicious links has been incorpored into a Testnet Informations 

As a connected User, you can report any of Published Testnet from the App. Of course, a reported Testnet will be notify to all admin. After Admin's Testnet review, Admin will decide if Testnet need to be deleted or published again.
Of course, a Testnet 's Author cannot report his own Testnet, it does not make any sense!

![user stories test](static/assets/images/readme-images/userstories19.png)

* As a Site User  I will receive information as Notifications when a Testnet that I copied have been updated by the author so I can check it out what is updated 

As a connected User who has copied Testnet from other User, you will receive a notification each time a Copied Testnet has been updated by the author. It will allow you to keep on track with the newest tasks to do for this Testnet.

![user stories test](static/assets/images/readme-images/userstories20.png)


* As a Site User  I can see the most popular Testnet of the App, which means the most copied Testnet by other users  

In my view, the more a Testnet is copied, the more popular it becomes within the app. So, as a connected User, you can display all the most copied Testnet on the App :

![user stories test](static/assets/images/readme-images/userstories21.png)


* As a Site User  I can Display the informations about any **none Reported** Testnet of the App   

As a connected User, you can display all the Testnet of the App except the reported one.
All the created Testnet on the app are available for publishing and are visible for anyone connected to the App (except blocked users)

*  As a Site User  I can have an access to all my testnet(s) and I can see a different coloring design on each to get to know the difference between "Original", "Copied" or "Reported"   

As a connected User, you have access to "Show My Testnet" where you will see all your Testnet :
- Original (blue color)
- Copy by you (Yellow color)
- Testnet from other, not copied yet by you (Grey color)-> This appears only if you search for a testnet

![user stories test](static/assets/images/readme-images/userstories23.png)

![user stories test](static/assets/images/readme-images/userstories22.png)

* As a Site User  I can see an information box with the successful result of any significant actions within the app   

As a connected User, you will have a displayed message each time you execute a significant action within the app as :

- Creation of a Testnet
- Copy of a Testnet
- Follow a User
- Unfollow a user
- Edit your profile
- Update a Testnet
- Delete a Testnet
- Report a Testnet

This message is displayed always at the same place on the page :

![user stories test](static/assets/images/readme-images/userstories24.png)

[Back to top](<#table-of-content>)


**As an Admin** :

* As a Site Admin  I can log in and out  

Same as a normal User.

* As a Site Admin  I can create, edit and delete a testnet of mine and from others   

Same as a normal User but with an extra privilege for other's Testnet management.
An Admin can delete Testnet from others, but cannot edit the user informations inside the Testnet.
An admin cannot create a Testnet with an Other User as Author.

![user stories test](static/assets/images/readme-images/userstories25.png)


* As a Site Admin  I can have access to a admin board to manage Testnets and users of the app 

As an Admin, you can access to 2 new buttons on dashboard which are :
- Board users
- Board Testnet(s)

![user stories test](static/assets/images/readme-images/userstories26.png)

* As a Site Admin  I can display all reported Testnet on the Testnet Board  

As an admin, you can access to a special section called "Board Testnet(s)" where you can see all the reported Testnet.

* As a Site Admin  I can cancel report on reported testnet and report none reported testnet   

As an Admin, you can cancel report on reported Testnet and on the oposite report a Testnet.
This action is made on "Board Testnet(s)" Section.

*  As a Site Admin  I can give admin role to a normal user    

As an admin, you can give admin role to an other User only if this User is not blocked.

*  As a Site Admin  I can block users and delete users  

As an Admin, you can block a User or Unblock a User. Also, an Admin can delete a User only if the User is already blocked. For more information, please refer to the following section of this documentation : Delete a User from the App


*  As a Site Admin  I can kick out a user from admin role 

As an Admin, you can kick out a user from admin role at any time. There is a button called "Kick as Admin" on "Board Users" section.

*  As a Site Admin  I can change my profile informations such as avatar, bio etc..  

Exactly as a normal User.

* As a Site Admin  I can receive specific notifications about a reported testnet   

As an Admin, I will receive notification(s) when some specific event happens as :

- A testnet have been reported


![user stories test](static/assets/images/readme-images/userstories27.png)

[Back to top](<#table-of-content>)


## Validator HTML CSS PYTHON


