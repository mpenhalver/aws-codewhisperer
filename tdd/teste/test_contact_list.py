import unittest
from module.contact_list import ContactList

class TestContactList(unittest.TestCase):
    def setUp(self):
        self.contact_list = ContactList()
        self.contact_list.add_contact("Iron Man", "123-456-789", "ironman@mail.com")
        self.contact_list.add_contact("Captain America", "987-654-321", "captainamerica@mail.com")
        self.contact_list.add_contact("Thor", "555-555-555", "thor@mail.com")

    def test_add_contact(self):
        self.contact_list.add_contact("Hulk", "789-654-321", "hulk@mail.com")
        self.assertEqual(self.contact_list.contacts[3],{"name": "Hulk", "phone_number": "789-654-321", "email": "hulk@mail.com"})

    def test_get_contact(self):
        self.assertEqual(self.contact_list.get_contacts(),
            [
                {"name": "Iron Man", "phone_number": "123-456-789", "email": "ironman@mail.com"},
                {"name": "Captain America", "phone_number": "987-654-321", "email": "captainamerica@mail.com"},
                {"name": "Thor", "phone_number": "555-555-555", "email": "thor@mail.com"}
            ]
        )
    
    def test_remove_contact(self):
        self.contact_list.add_contact("Magneto", "123-456-789", "magneto@mail.com")
        self.contact_list.remove_contact("Magneto")
        self.assertNotIn("Magneto", self.contact_list.contacts)
