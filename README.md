# For team mates
Note: Everyone is free to edit this README as well to share resources and document important changes for others to read.
Whenever a new use case is being worked on, create a new branch, and only merge it with the master branch when the code passes the tests you've written for. When addional code is added to our master branch, we assume the pre-existing code already works. For any help for using git, feel free to drop me (junde) a question :D

### Recent Changes (9/2/19)
- Rewritten website using Django (sorry again for not agreeing on this earlier).
  - Website currently contains 2 folders
    - my_project contains the network and website settings
    - templates contains html files that are displayed when we load the site
  - To run website locally, get into website/ dir and execute:
    python3 manage.py runserver
  - Created an account using Django's native user management system. This is the only account that we can log into at the moment.
    Username: superuser
    Password: 1234
    Email address: test.email.com
- As we'll have to display the usage of the website across multiple users at the same time, it would be a better idea to host the website somewhere instead of locally. To this end I recommend we use a free service called Heroku to do this (to be implemented).
- As each of us have different python modules (including the server in Heroku), it is a good time to learn about Dockers, a solution that abstracts dependencies, and any codes required to run prior to the start of the website. With dockers the website, we script the downloading of dependencies and run any codes that is required prior to the set up of the website once, so that in the future we can kickstart websites with just a line of code. This is still something I'm working on, but it will be a good idea for you to read some guides below to get an idea of what Dockers is about.

### Getting Around
- Documentations and project requirements are stored in ./Documentation
- I'll be leaving my logs in ./Documentation, feel free to leave yours inside as well

### Considerations
- Possibly host web page on heroku when displaying to client
- Possibly use PivotalTracker to keep track of code progress
- Possibly automate creation of issues on Github
- Possibly automate creation of statistics based on the forms that are filled

### Resources
- Google Drive
https://drive.google.com/open?id=1nejQR1brcVUTHJ9_bi_PhdwTtDLdx0zn

### Guides
- Creating log-in page
https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/
- Introduction to Model-Template-View architecture of websites
https://djangobook.com/mdj2-django-structure/
- Using Django's native user authentication system
https://docs.djangoproject.com/en/2.1/topics/auth/default/
- Jun De's notes for Dockers
https://docs.google.com/document/d/1GTbBhWj93e7oUoBi-i61dFe4V-oUggdwZ14g6ruBGlA/edit?usp=sharing
- Docker's beginner guide
https://docs.docker.com/get-started/part2/
- Using JWT authentication on Django framework
https://simpleisbetterthancomplex.com/tutorial/2018/12/19/how-to-use-jwt-authentication-with-django-rest-framework.html
- Other open sourced versions of Django helpdesks 
https://django-helpdesk.readthedocs.io/en/master/index.html

