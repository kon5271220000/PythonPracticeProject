import csv

class Contact:
    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail

    def __str__(self) -> str:
        return f"Name: {self.name}, phone: {self.phone}, mail = {self.mail}"
    

class ContactBook:
    def __init__(self, filename='05_ContactBook/contacts.csv') -> None:
        self.contacts = []
        self.filename = filename
        self.load_from_csv()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_to_csv()

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                self.save_to_csv() 

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
            else:
                return None
    
    def display_contact(self):
        for contact in self.contacts:
            print(contact)

    def save_to_csv(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])  # Writing headers
            for contact in self.contacts:
                writer.writerow([contact.name, contact.phone, contact.mail])
        print("Contacts saved to", self.filename)

    def load_from_csv(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row:  # Ensure the row is not empty
                        contact = Contact(row[0], row[1], row[2])
                        self.add_contact(contact)
            print("Contacts loaded from", self.filename)
        except FileNotFoundError:
            print(f"{self.filename} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("Contact book menu:")
        print("1-Add contact")
        print("2-Delete contact")
        print("3-search contact")
        print("4-view all contact")
        print("5-exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)
            print("contact added")
        elif choice == "2":
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)
            print("contact deleted")
        elif choice == "3":
            name = input("Enter name to search: ")
            contact = contact_book.search_contact(name)
            if contact:
                print("contact found:")
                print(contact)
        elif choice == "4":
            contact_book.display_contact()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("invalid value, try again")
            
        
if __name__ == "__main__":
    main()