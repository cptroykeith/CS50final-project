# Roy's Final CS50 Project

### Video Demo
[Link to youtube](https://youtu.be/XkvOrpTwquI)


#### Description
**This is a command line project (login and signup system)**
1. >signup
  - A User is required to signup by creating a *username,password and confirm the password*.
  - If the password doesn't match or the password is less than seven characters, the user will be notified that ("password does not match, restart" OR "password too short, restart:" respectively)
   - If the user is using a username that is already in use, they are notified that ("Username exists, restart")
   - If the *username and password* are fine, the system informs the user that its a "success" and the information is stored in a text file database.
2. >Login
    - A user is required to enter their *username and password*
    - If the *password and username* are equal to the ones in the database text file the system notifies the user that "Login successfull").    
    - If the *password and username* are equal to the ones in the database text file,the system notifies the user that ("Login successfull" and "Hi,",Username).
    - And if the *username and password* don't match the ones in the database text file,the system will notify the user that ("password or Username is incorrect").
    - Or if the *username and password* are not in the data the system notifies the user that ("username or password doesn't exist").
    - If the user doesn't fill in the required information the system will notify them that ("please enter a value") .
   