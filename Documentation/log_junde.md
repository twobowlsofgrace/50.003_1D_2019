##### 11/3
- Managed to set up mysql on django with zhaohong's help
- Run
```sudo apt-get install mysql-server```
- If you cant log in, try finding account info of "debian-sys-maint" and log in using that, it has root privileges and can let you reset root password
- If you're logging in root, run
```sudo mysql -u root -p```
then insert new password
- Create new user (according to our settings.py) and new database `50003`. Rmb use ` .
- run
```
$ pip3 install mysqlclient
$ python3 manage.py migrate
$ python3 manage.py runserver
```



##### 3/3
- Tried to use docker to set up mysql, died so hard am gna continue some other time
- Used mysql base but when i run docker image there's no response, even when i get the port right. I suspect running mysql docker runs something else that i do not know of, need to find out more
- Next step: Run docker without mysql, then mysql with appropriate RUN and CMDs to know how to use mysql base images better
- Now i'm setting up mysql to run the website without docker first
https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
- ok because i forgot my mysql passoword, this itself is also cancer. tried burning and reinstalling but didnt work. consider using docker or burn ubuntu and install xubuntu and shunbian reinstall mysql
https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
https://www.digitalocean.com/community/tutorials/how-to-install-the-latest-mysql-on-ubuntu-16-04#step-2-—-installing-mysql


##### 26/2
- Fixed finding of "create profile" template. Redid login as a separate app.
- Creating user: {username: user1, password: 1234, ID:1, email:boi@gmail.com, phonenumber:87654321}
- Creation of user is successful, missing a couple of possible errors (same username, password checking etc.)


##### 24/2
- I realised login, and home page should belong in a separate app, instead of being in the website/ dir. 
- Need to write app for home, log-in and then account creation
https://docs.djangoproject.com/en/2.1/intro/tutorial03/

##### 19/2
- Currently server has issues opening create-user.index i think the problem lies in the DIRs that the bootloader is looking at. Might have to configure the DIR in TEMPLATES of settings.py to accomodate apps other than the main log-in page. But must be able to revert to original cos settings.py is used by the rest of the team.

##### 16/2
- Learning how Users work, and creating notes for User management
- Halfway through creating the form for account creation (Just created Form class). Taking reference from:
https://docs.djangoproject.com/en/2.1/topics/forms/

##### 8/2
- Created web interface to log-in and log out using the following guide
https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
- Will need to work on hosting website on heroku, and dependencies taken care of by docker. To implement these with Django, use the following guides:
https://docs.docker.com/compose/install/
https://docs.docker.com/compose/django/

##### 29/1
- Each of us are to create our own questions to clarify our project requirements by tonight 2359. I am to contact the client in Accenture to prepare a day to ask questions.

##### 28/1
- Project 2 is chosen, done in Python. None of us are experienced/interested in game development. Zhao hong has experience in web development (Python Flask/Django)
