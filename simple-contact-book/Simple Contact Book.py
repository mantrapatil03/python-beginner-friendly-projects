class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def show_contacts(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")


# Example usage
contact_book = ContactBook()
contact_book.add_contact(Contact("Shree", "123-456-7890"))
contact_book.add_contact(Contact("Ram", "987-654-3210"))

contact_book.show_contacts()
