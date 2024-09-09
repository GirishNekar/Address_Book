"""
@Author: Girish
@Date: 2024-09-09
@Last Modified by: Girish
@Last Modified time: 2024-09-09
@Title : Ability to add, edit, delete, and manage multiple Contacts in Address Book
"""

import re
import mylogging as log

logger = log.logger_init('UC6')

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

class AddressBook:
    """
    Class: AddressBook
    Manages a collection of ContactPerson objects and user interactions.
    """
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        """
        Function: Add a new contact to the Address Book by collecting user input.
        
        Parameter: self
        
        Returns: None
        """
        first_name = self.validate_input("Enter first name (Eg : Girish): ", r'^[A-Z][A-Za-z]{2,}$', "Invalid first name. Please use only letters.")
        last_name = self.validate_input("Enter last name(Eg : Nekar): ", r'^[A-Z][A-Za-z]{2,}$', "Invalid last name. Please use only letters.")
        address = input("Enter address: ")
        city = self.validate_input("Enter city: ", r'^[A-Za-z\s]+$', "Invalid city name. Please use only letters.")
        state = self.validate_input("Enter state: ", r'^[A-Za-z\s]+$', "Invalid state name. Please use only letters.")
        zip_code = self.validate_input("Enter zip code: ", r'^\d{6,}$', "Invalid zip code. Please enter a 6-digit number.")
        phone_number = self.validate_input("Enter phone number(Eg : 87 4567890654): ", r'^\d{2} \d{10}$', "Invalid phone number. Please enter a 10-digit number.")
        email = self.validate_input("Enter email(Eg : gmnekar45@gmail.com): ", r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', "Invalid email format.")

        contact = ContactPerson(first_name, last_name, address, city, state, zip_code, phone_number, email)
        self.contacts.append(contact)
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
            for index, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {index}:\n{contact}")

    def edit_contact(self):
        """
        Function: Edit an existing contact's details based on their first name.
        
        Parameter: self
        
        Returns: None
        """
        first_name = input("Enter the first name of the contact you want to edit: ")
        for contact in self.contacts:
            if contact.first_name == first_name:
                print("\nCurrent details of the contact:")
                print(contact)
                print("\nEnter new details (leave blank to keep current value):")

                new_last_name = input(f"New Last Name (Current: {contact.last_name}): ") or contact.last_name
                new_address = input(f"New Address (Current: {contact.address}): ") or contact.address
                new_city = input(f"New City (Current: {contact.city}): ") or contact.city
                new_state = input(f"New State (Current: {contact.state}): ") or contact.state
                new_zip_code = input(f"New Zip Code (Current: {contact.zip_code}): ") or contact.zip_code
                new_phone_number = input(f"New Phone Number (Current: {contact.phone_number}): ") or contact.phone_number
                new_email = input(f"New Email (Current: {contact.email}): ") or contact.email

                # Update the contact with new details
                contact.last_name = new_last_name
                contact.address = new_address
                contact.city = new_city
                contact.state = new_state
                contact.zip_code = new_zip_code
                contact.phone_number = new_phone_number
                contact.email = new_email

                logger.info(f"Contact {first_name} updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self):
        """
        Function: Delete a contact from the Address Book based on their first name.
        
        Parameter: self
        
        Returns: None
        """
        first_name = input("Enter the first name of the contact you want to delete: ")
        for index, contact in enumerate(self.contacts):
            if contact.first_name == first_name:
                del self.contacts[index]
                logger.info(f"Contact {first_name} deleted successfully.")
                return
        print("Contact not found.")

    @staticmethod
    def validate_input(prompt, pattern, error_message):
        """
        Function: Validate user input based on a provided regular expression pattern.

        Parameters:
            prompt : The prompt message to display to the user.
            pattern : The regular expression pattern to validate input against.
            error_message : The error message to display if input is invalid.

        Returns:
            str: The validated input from the user.
        """
        for attempts in range(3):
            user_input = input(prompt)
            if re.match(pattern, user_input):
                return user_input
            print(error_message)
        logger.info("Session expires, try again after some time.")
        

    def manage(self):
        """
        Function: Handles user interactions for managing the Address Book.
        
        Parameter: None
        
        Returns: None
        """
        while True:
            print("\nMenu:")
            print("1. Add a new contact")
            print("2. Add multiple contacts")
            print("3. Display all contacts")
            print("4. Edit an existing contact")
            print("5. Delete a contact")
            print("6. Exit")
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
                print("Exiting the Address Book")
                break
            else:
                print("Invalid choice. Please try again.")

class AddressBookManager:
    """
    Class: AddressBookManager
    Manages multiple AddressBook instances, each identified by a unique name.
    """
    def __init__(self):
        self.address_books = {}

    def create_address_book(self):
        """
        Function: Create a new Address Book with a unique name.
        
        Parameter: self
        
        Returns: None
        """
        name = input("Enter the name for the new Address Book: ").strip()
        if name in self.address_books:
            print("An Address Book with this name already exists.")
        else:
            self.address_books[name] = AddressBook()
            logger.info(f"Address Book '{name}' created successfully.")

    def select_address_book(self):
        """
        Function: Select an Address Book from the available Address Books.
        
        Parameter: self
        
        Returns: AddressBook instance
        """
        if not self.address_books:
            print("No Address Books available.")
            return None

        print("Available Address Books:")
        for index, name in enumerate(self.address_books, start=1):
            print(f"{index}. {name}")

        choice = input("Enter the number of the Address Book you want to manage: ")
        try:
            index = int(choice) - 1
            name = list(self.address_books.keys())[index]
            return self.address_books[name]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            return None

    def manage(self):
        """
        Function: Handles user interactions for managing Address Books and their contacts.
        
        Parameter: None
        
        Returns: None
        """
        while True:
            print("\nMenu:")
            print("1. Create a new Address Book")
            print("2. Manage an existing Address Book")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_address_book()
            elif choice == '2':
                address_book = self.select_address_book()
                if address_book:
                    address_book.manage()
            elif choice == '3':
                print("Exiting Address Book Manager")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    manager = AddressBookManager()
    manager.manage()

if __name__ == "__main__":
    main()
