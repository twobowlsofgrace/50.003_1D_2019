import unittest
from django.contrib.auth.models import User
from django.test import RequestFactory,TestCase,Client
from .models import Ticket
from .views import create
from django.urls import reverse


##Example
##class AnimalTestCase(TestCase):
##    def setUp(self):
##        Animal.objects.create(name="lion", sound="roar")
##        Animal.objects.create(name="cat", sound="meow")
##
##    def test_animals_can_speak(self):
##        """Animals that can speak are correctly identified"""
##        lion = Animal.objects.get(name="lion")
##        cat = Animal.objects.get(name="cat")
##        self.assertEqual(lion.speak(), 'The lion says "roar"')
##        self.assertEqual(cat.speak(), 'The cat says "meow"')
##
##
##

# class CreateTicketTestCase(unittest.TestCase):
#     def setUp(self):
#         # Maybe we don't need this for testing ticket creation
#         # c = Client()
#         # c.force_login(username='john',password:'smith')
#         # response = c.post('/login/',{'username': 'john', 'password': 'smith'})
#         # print("Response status code")
#         # response.status_code
#         # simulate effect of user logging into site
#         # also forces a user to be logged in aka without authenticating
#
#         # Create a ticket
#         self.user = User.objects.create_user(username='john',password='12345')
#         ticket = Ticket.objects.create(ticket_id="12345678910", title="Forgot my username",
#                               description="I am very bad at remembering",
#                               user="john")
#         self.factory = RequestFactory()
#
#
#     def test_create_valid_ticket(self):
#         title = Ticket.objects.get(title="Forgot my username")
#         description = Ticket.objects.get(description="I am very bad at remembering")
#         request = self.factory.get('/createticket')
#         request.user = self.user
#         response = create(request)
#         self.assertEqual(response.status_code,200)

class TicketCreationViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create(self):
        url = reverse('create')
        response = self.client.get(url)
        self.assertEqual(response.status,200)
        response = self.client.post(url,{})
        self.assertEqual(response.status,200)
        req_data = {'user':'john',
                       'title':'@@@',
                       'description':'fk mah life'}
        response = self.client.post(url, req_data)
        self.assertEqual(response.status,200)






