from django.core import mail
from django.test import TestCase
from django.conf import settings



class EmailTest(TestCase):
    def test_send_email(self):
        # Send message.
        mail.send_mail('Subject here', 'Here is the message.',
            settings.EMAIL_HOST_USER, ['receiver@example.com'],
            fail_silently=False)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Subject here')

    def test_mail_admins(self):
        mail.mail_admins('Subject here','Here is the message',
                         fail_silently=False)

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)

        # Verify that the subject of the first message is correct.
        #self.assertEqual(mail.outbox[0].subject, 'Subject here')

