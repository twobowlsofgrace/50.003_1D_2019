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
    size = models.IntegerField()  # for first row, this represents total number of tickets, for other rows it represents number of replies (including ticket itself, starting from 0) for that ticket
    creator = models.CharField(max_length=20)  # user
    addressed_by = models.CharField(max_length=20)  # admin
    resolved_by = models.CharField(max_length=20)  # if None, ticket is not resolved
    read_by = models.CharField(max_length=100)  # to have names of admins that read the ticket to be concaternated to this value
    queue_number = models.IntegerField()  # to be implemented in future

class Ticket_Details(models.Model):
    # represent model that contains all replies and tickets
    ticket_id = models.IntegerField(max_length=20)  # represent unique id of ticket in All_Tickets
    thread_queue_number = models.IntegerField(max_length=20)  # in a thread (of replies under a ticket, queue number represents the order of replies, starting from 0 (the original ticket itself))
    author_id = models.IntegerField(max_length=20)  # represent id of the user, stated in the table 'createuser_extended_user' in database 50003
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=256)
    image = models.ImageField(max_length=100)  # to be implemented
    file = models.FileField()  # to be implemented

