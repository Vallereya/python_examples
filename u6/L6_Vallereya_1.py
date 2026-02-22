"""
    Program Name:   Login System
    Author:         Vallereya
    Date:           2025-02-22
    Starter Code:   N/A
    Purpose:        This program will simulate a simple
                    login system using a dictionary to 
                    store usernames and passwords.
"""

def main():

    # Creating a dictionary to store usernames and passwords.
    users = {
        "guest": "guest",
        "admin": "admin",
    }

    # Prompt user for username.
    username = input("Enter username: ").strip()

    # Check if the username exists. 
    if username not in users:
        print("Incorrect username, please try again.")
        return
    
    # Set a maximum number of attempts for password.
    max_attempts = 3

    for attempts_num in range(1, max_attempts + 1):
        password = input("Enter password: ")

        # Check if the password is correct.
        if password == users[username]:

            # Determine security level based on username.
            if username == "guest":
                security_level = "Guest"
                print(f"\nWelcome, {username}. You have Guest access.")
            else:
                security_level = "Security Level 1"
                print(f"\nWelcome, {username}. You have {security_level}.")
            return

if __name__ == "__main__":
    main()
