# For team mates
Note: Everyone is free to edit this README as well to share resources and document important changes for others to read.
Whenever a new use case is being worked on, create a new branch, and only merge it with the master branch when the code passes the tests you've written for. When addional code is added to our master branch, we assume the pre-existing code already works. For any help for using git, feel free to drop me (junde) a question :D

### Creating accounts for your own use (12/3/19)
```
$ python manage.py createsuperuser --username=joe --email=joe@example.com
```

### To test connection between TestForm and Source websites (27/3/19)
Purpose of the creation of TestForm: To automate creation of tickets through submitting forms in a separate website. NOTE: User account has not been created yet.

In one console, run the Source website in port 3000
```
$ python3 manage.py runserver 3000
```
In another console, run the TestForm website in port 4000
```
$ python3 manage.py runserver 4000
```


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

