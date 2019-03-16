##### 15/3
Helpful features in ticketing systems (Source:https://www.teamsupport.com/blog/must-have-help-desk-ticketing-system-features)
1. Ticket automation – This is an absolute must have for any help desk ticketing system, regardless of the industry. Automation can perform many tasks, from reminding you that a ticket response is needed to routing a ticket to a specific user, and so much more.
2. SLA (Service Level Agreement) status information – The first time an employee looks at a ticket, they attempt to gauge its urgency and prioritize among other tickets. With direct help desk SLA information right in the ticketing system, it’s easier to prioritize tickets and avoid SLA violations.
3. Ticket tags – These allow for easy organization of tickets and you can quickly spot popular or common issues. They can also be of great value directly within tickets by automatically recommending Knowledge Base articles depending on the tags assigned.
4. Customizable ticket templates – Not all tickets are the same. Choose a system where you can create several templates that can be loaded on command to make responding to tickets even easier. These templates can also be combined as needed if the ticket has multiple questions.
5. Individual ticket queues – Even now, so many companies are all working out of the same ticket queue. With individual queues, your employees can organize their tickets to be more efficient and can even look at the queues of their colleagues to see who needs help.
6. Customizable ticket status options – Life isn’t “open and closed” and neither is ticketing. Make sure you have a system with many status options that you can customize for your business. Emails can also be triggered to send to customers automatically when a status changes.
7. Public and private actions on tickets – Not all ticket conversations need to be seen by a customer. That also doesn’t mean they should happen internally over IM. Keep ticket conversations in the system with private actions until you’re ready for a public customer action.
8. Product and inventory association – Product and inventory management is a lifesaver for any company that deals with physical or virtual products. Instead of digging through external documents, it’s easy to track this information for each customer so it shows up directly on their ticket page.
9. Personalized ticket pages by customer – The more employees know about your customer, the better they will be at resolving their issues. Customized ticket pages can show information including how satisfied the customer is, how many tickets they have open, and much more.
10. Related Tickets – All help desk pros have been bombarded in the past with an increase of simple, repetitive requests and the long process of answering them all individually. With related tickets it’s easy to aggregate these requests and reply to them all at once to save time.
11. Ticket deflection – What if your employees spot a customer request that can be easily answered with a Knowledge Base article? Don’t make them go find the link, have built-in ticket deflection capabilities on ticket pages to grab the right link quickly.
12. Customizable ticket submission form – While not directly within a help desk ticketing system, choosing a system that allows for customized fields in customer-facing ticket forms is vital for capturing the information you need. This can drastically reduce the amount of basic follow-up questions and speed ticket resolution time.




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
- Implementing pass test case for createuser now (in /Source/website/createuser/tests.py)
Test was not detected when ```python3 manage.py test createuser``` is run
https://docs.djangoproject.com/en/2.1/intro/tutorial05/


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
