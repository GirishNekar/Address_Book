"""
@Author: Girish
@Date: 2024-09-09
@Last Modified by: Girish
@Last Modified time: 2024-09-09
@Title : Ability to add, edit, delete, and manage multiple Contacts in Address Book and search based on the 
"""

import re
import mylogging as log

logger = log.logger_init('UC7')

class ContactPerson:
    """
    Class: ContactPerson
    Represents a contact person with details such as first name, last name, address, city, state, zip, phone number, and email.
    """
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return (
            f"Name: {self.first_name} {self.last_name}\n"
            f"Address: {self.address}, {self.city}, {self.state} - {self.zip_code}\n"
            f"Phone Number: {self.phone_number}\n"
            f"Email: {self.email}"
        )

    def __eq__(self, other):
        if isinstance(other, ContactPerson):
            return self.first_name == other.first_name
        return False

    def __hash__(self):
        return hash(self.first_name)

class AddressBook:
    """
    Class: AddressBook
    Manages a collection of ContactPerson objects and user interactions.
    """
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        """
        Function: Add a new contact to the Address Book by collecting user input.
        
        Parameter: self
        
        Returns: None
        """
        first_name = self.validate_input("Enter first name (Eg : Girish): ", r'^[A-Z][A-Za-z]{2,}$', "Invalid first name. Please use only letters.")
        last_name = self.validate_input("Enter last name (Eg : Nekar): ", r'^[A-Z][A-Za-z]{2,}$', "Invalid last name. Please use only letters.")
        address = input("Enter address: ")
        city = self.validate_input("Enter city: ", r'^[A-Za-z\s]+$', "Invalid city name. Please use only letters.")
        state = self.validate_input("Enter state: ", r'^[A-Za-z\s]+$', "Invalid state name. Please use only letters.")
        zip_code = self.validate_input("Enter zip code: ", r'^\d{6,}$', "Invalid zip code. Please enter a 6-digit number.")
        phone_number = self.validate_input("Enter phone number (Eg : 87 4567890654): ", r'^\d{2} \d{10}$', "Invalid phone number. Please enter a 10-digit number.")
        email = self.validate_input("Enter email (Eg : gmnekar45@gmail.com): ", r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', "Invalid email format.")

        contact = ContactPerson(first_name, last_name, address, city, state, zip_code, phone_number, email)
        
        # Check for duplicate contact based on first name
        if first_name in self.contacts:
            print("A contact with this first name already exists.")
            logger.info(f"Attempted to add duplicate contact with first name: {first_name}")
        else:
            self.contacts[first_name] = contact
            logger.info("Contact added successfully.")

    def add_multiple_contacts(self):
        """
        Function: Add multiple contacts to the Address Book by collecting user input repeatedly.
        
        Parameter: self
        
        Returns: None
        """
        while True:
            print("\nAdding a new contact.")
            self.add_contact()
            more_contacts = input("Do you want to add another contact? (yes/no): ").strip().lower()
            if more_contacts != 'yes':
                break

    def display_contacts(self):
        """
        Function: Display all contacts in the Address Book.
        
        Parameter: self
        
        Returns: None
        """
        if not self.contacts:
            print("Address Book is empty.")
        else:
            for index, contact in enumerate(self.contacts.values(), start=1):
                print(f"\nContact {index}:\n{contact}")

    def edit_contact(self):
        """
        Function: Edit an existing contact's details based on their first name.
        
        Parameter: self
        
        Returns: None
        """
        first_name = input("Enter the first name of the contact you want to edit: ")
        if first_name in self.contacts:
            contact = self.contacts[first_name]
            print("\nCurrent details of the contact:")
            print(contact)
            print("\nEnter new details (leave blank to keep current value):")
            new_first_name = input(f"New First Name (Current: {contact.first_name}): ") or contact.first_name
            new_last_name = input(f"New Last Name (Current: {contact.last_name}): ") or contact.last_name
            new_address = input(f"New Address (Current: {contact.address}): ") or contact.address
            new_city = input(f"New City (Current: {contact.city}): ") or contact.city
            new_state = input(f"New State (Current: {contact.state}): ") or contact.state
            new_zip_code = input(f"New Zip Code (Current: {contact.zip_code}): ") or contact.zip_code
            new_phone_number = input(f"New Phone Number (Current: {contact.phone_number}): ") or contact.phone_number
            new_email = input(f"New Email (Current: {contact.email}): ") or contact.email

            # Update contact details
            updated_contact = ContactPerson(new_first_name, new_last_name, new_address, new_city, new_state, new_zip_code, new_phone_number, new_email)
            self.contacts[first_name] = updated_contact

            logger.info(f"Contact {first_name} updated successfully.")
        else:
            print("Contact not found.")

    def delete_contact(self):
        """
        Function: Delete a contact from the Address Book based on their first name.
        
        Parameter: self
        
        Returns: None
        """
        first_name = input("Enter the first name of the contact you want to delete: ")
        if first_name in self.contacts:
            del self.contacts[first_name]
            logger.info(f"Contact {first_name} deleted successfully.")
        else:
            print("Contact not found.")

    @staticmethod
    def validate_input(prompt, pattern, error_message):
        """
        Function: Validate user input based on a regular expression pattern.
        
        Parameter: 
        - prompt (str): The prompt to display to the user.
        - pattern (str): The regular expression pattern to validate the input.
        - error_message (str): The error message to display for invalid input.
        
        Returns: str
        """
        while True:
            user_input = input(prompt).strip()
            if re.match(pattern, user_input):
                return user_input
            else:
                print(error_message)

    def manage(self):
        """
        Function: Manage the Address Book system, providing options to add, display, edit, or delete contacts.
        
        Parameter: self
        
        Returns: None
        """
        while True:
            print("\nAddress Book Menu:")
            print("1. Add Contact")
            print("2. Add Multiple Contacts")
            print("3. Display Contacts")
            print("4. Edit Contact")
            print("5. Delete Contact")
            print("6. Go Back")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.add_multiple_contacts()
            elif choice == '3':
                self.display_contacts()
            elif choice == '4':
                self.edit_contact()
            elif choice == '5':
                self.delete_contact()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

class AddressBookManager:
    """
    Class: AddressBookManager
    Manages multiple Address Books, allowing creation, selection, and management of individual Address Books.
    """
    def __init__(self):
        self.address_books = {}

    def create_address_book(self):
        """
        Function: Create a new Address Book and add it to the manager.
        
        Parameter: self
        
        Returns: None
        """
        name = input("Enter the name of the new Address Book: ")
        if name in self.address_books:
            print("Address Book already exists.")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address Book '{name}' created successfully.")

    def select_address_book(self):
        """
        Function: Select an Address Book by name and manage it.
        
        Parameter: self
        
        Returns: None
        """
        if not self.address_books:
            print("No Address Books available. Please create one first.")
            return

        print("\nAvailable Address Books:")
        for index, name in enumerate(self.address_books.keys(), start=1):
            print(f"{index}. {name}")

        choice = input("Enter the number of the Address Book you want to select (or 'q' to quit): ")
        if choice.lower() == 'q':
            return

        try:
            index = int(choice) - 1
            if 0 <= index < len(self.address_books):
                selected_name = list(self.address_books.keys())[index]
                address_book = self.address_books[selected_name]
                print(f"Selected Address Book: {selected_name}")
                address_book.manage()
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def search_contacts(self):
        """
        Function: Search for contacts by city or state across all Address Books.
        
        Parameter: self
        
        Returns: None
        """
        search_type = input("Search by (1) City or (2) State? Enter 1 or 2: ")
        if search_type not in {'1', '2'}:
            print("Invalid choice.")
            return

        search_term = input("Enter the search term: ").strip()

        found_contacts = []
        for address_book_name, address_book in self.address_books.items():
            for contact in address_book.contacts.values():
                if (search_type == '1' and contact.city.lower() == search_term.lower()) or \
                   (search_type == '2' and contact.state.lower() == search_term.lower()):
                    found_contacts.append((address_book_name, contact))

        if found_contacts:
            print("\nSearch Results:")
            for book_name, contact in found_contacts:
                print(f"\nAddress Book: {book_name}")
                print(contact)
        else:
            print("No contacts found.")

    def manage(self):
        """
        Function: Manage the Address Book Manager, providing options to create, select, search Address Books.
        
        Parameter: self
        
        Returns: None
        """
        while True:
            print("\nAddress Book Manager Menu:")
            print("1. Create Address Book")
            print("2. Select Address Book")
            print("3. Search Contacts")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_address_book()
            elif choice == '2':
                self.select_address_book()
            elif choice == '3':
                self.search_contacts()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = AddressBookManager()
    manager.manage()
