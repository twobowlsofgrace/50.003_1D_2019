from django.db import models


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=30)
    title = models.CharField(max_length=60)
    resolved = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    description = models.CharField(max_length=256)
    user = models.CharField(max_length=60)

class All_Tickets(models.Model):
    # note: each model has its primary key, which increments as new elements are added, and the new number forms the element's id
    size = models.IntegerField()  # represents number of replies in each ticket
    creator = models.IntegerField()  # id of user
    addressed_by = models.IntegerField()  # id of admin
    resolved_by = models.IntegerField()  # if None, ticket is not resolved
    read_by = models.CharField(max_length=100)  # to have concaternated ids of admins (delimited by ",") that read the ticket to be concaternated to this value. I chose not to create new table as i needed to push for progress, otherwise that is defo prefered
    queue_number = models.IntegerField()  # to be implemented in future
    dateTime_created = models.DateTimeField()

class Ticket_Details(models.Model):
    # represent model that contains all replies and tickets
    ticket_id = models.IntegerField()  # represent unique id of ticket in All_Tickets
    thread_queue_number = models.IntegerField()  # in a thread (of replies under a ticket, queue number represents the order of replies, starting from 0 (the original ticket itself))
    author = models.IntegerField()  # represent id of the user, stated in the table 'createuser_extended_user' in database 50003
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=256)
    image = models.ImageField(max_length=100)  # to be implemented
    file = models.FileField()  # to be implemented
    dateTime_created = models.DateTimeField()
