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

    # Creating a dictionary to store usernames.
    users = {
        "guest": "guest",
        "admin": "admin",
    }

    username = input("Enter username: ").strip()

    if username not in users:
        print("Incorrect username, please try again.")
        return
    
    max_attempts = 3

if __name__ == "__main__":
    main()
