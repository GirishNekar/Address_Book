"""
@Author: Girish
@Date: 2024-09-09
@Last Modified by: Girish
@Last Modified time: 2024-09-09
@Title : UC2-Ability to add a new Contact to Address Book
"""

import re
import mylogging as log

logger = log.logger_init('UC2')

class ContactPerson:
    
    ## Represents a contact person with details such as first name, last name, address, city, state, zip, phone number, and email.
    
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

    # Manages a collection of ContactPerson objects and user interactions.
    
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        
        """
        Function: Add a new contact to the Address Book by collecting user input.
        
        Parameter : self
        
        Returns : None
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

    def display_contacts(self):
        """
        Function: Display all contacts in the Address Book.
        
        Parameter : self
        
        Returns : None
        """
        if not self.contacts:
            print("Address Book is empty.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"\nContact {index}:\n{contact}")

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
        
        Parameter : None
        
        Returns : None
        """
        

        while True:
            print("\nMenu:")
            print("1. Add a new contact")
            print("2. Display all contacts")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.display_contacts()
            elif choice == '3':
                print("Exiting the Address Book")
                break
            else:
                print("Invalid choice. Please try again.")

def main():
    address_book = AddressBook()
    address_book.manage()


if __name__ == "__main__":
    main()

