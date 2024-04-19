class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        self.contacts.append({
            'name': name,
            'phone_number': phone_number,
            'email': email
        })

    def get_contacts(self):
        return self.contacts
    
    def remove_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                break
