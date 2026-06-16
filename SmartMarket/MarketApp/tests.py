from django.test import TestCase

# Create your tests here.
from models import Contact
class ContactModelTest(TestCase):
    def setUp(self):
        Contact.objects.create(name='John Doe',
                               email='john.doe@example.com',
                               subject='Test Subject',
                               message='Test Message')
    def test_contact_creation(self):
        contact = Contact.objects.get(name='John Doe')
        self.assertEqual(contact.email, 'john.doe@example.com')
        self.assertEqual(contact.subject, 'Test Subject')
        self.assertEqual(contact.message, 'Test Message')

