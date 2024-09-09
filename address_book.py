import re
import mylogging as log

logger = log.logger_init('UC1')

def validate_input(prompt, pattern, error_message):
    """
    Function: Validate user input based on a provided regular expression pattern.

    Parameters:
        prompt: The prompt message to display to the user.
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
 



def main():
    
    print("Welcome to the Address Book!")
    
    contact = {}
    
    contact['First Name'] = validate_input("Enter first name (Eg : Girish): ", r'^[A-Z][A-Za-z]{2,}$', "Invalid first name. Please use only letters.")
    contact['Last Name'] = validate_input("Enter last name(Eg : Nekar): ", r'^[A-Z][A-Za-z]{2,}$', "Invalid last name. Please use only letters.")
    contact['Address'] = input("Enter address: ")
    contact['City'] = validate_input("Enter city: ", r'^[A-Za-z\s]+$', "Invalid city name. Please use only letters.")
    contact['State'] = validate_input("Enter state: ", r'^[A-Za-z\s]+$', "Invalid state name. Please use only letters.")
    contact['Zip'] = validate_input("Enter zip code: ", r'^\d{6,}$', "Invalid zip code. Please enter a 5-digit number.")
    contact['Phone Number'] = validate_input("Enter phone number(Eg : 87 4567890654): ", r'^\d{2} \d{10}$', "Invalid phone number. Please enter a 10-digit number.")
    contact['Email'] = validate_input("Enter email(Eg : gmnekar45@gmail.com): ", r'^[a-zA-Z0-9]+(?:[._%+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?$', "Invalid email format.")

    logger.info("\nContact created successfully!\n")
    
    for key, value in contact.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
