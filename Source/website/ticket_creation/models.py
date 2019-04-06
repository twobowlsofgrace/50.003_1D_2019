from django.db import models


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=30)
    title = models.CharField(max_length=60)
    resolved = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    description = models.CharField(max_length=256)
    user = models.CharField(max_length=60)

class All_Tickets(models.Model):
    id = models.IntegerField(max_length=20)  # to be determined by total number of tickets
    size = models.IntegerField(max_length=20)  # for first row, this represents total number of tickets, for other rows it represents number of replies (including ticket itself, starting from 0) for that ticket
    creator = models.CharField(max_length=20)  # user
    addressed_by = models.CharField(max_length=20)  # admin
    resolved_by = models.CharField(max_length=20)  # if None, ticket is not resolved
    read_by = models.CharField(max_length=100)  # to have names of admins that read the ticket to be concaternated to this value
    queue_number = models.IntegerField(max_length=20)  # to be implemented in future

class Ticket_Details(models.Model):
    id = models.IntegerField(max_length=20)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=256)
    image = models.ImageField(max_legnth=100)  # to be implemented
    file = models.FileField()  # to be implemented
