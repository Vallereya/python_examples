"""
    Program Name:   Dice Game
    Author:         Vallereya
    Date:           2025-02-15
    Starter Code:   N/A
    Purpose:        This program will simulate a simple
                    dice game. Roll two dice, display 
                    the dice + total, and print the term 
                    for that roll.
"""

import random

# Function to determine the term based 
# on the dice values.
def get_term(d1, d2):

    # Sort the dice to make it easier to 
    # check for specific combinations.
    a, b = sorted((d1, d2))

    total = d1 + d2

    # Terms based on specific dice values, 
    # order doesn't matter.
    if (a, b) == (1, 1):
        return "Snake Eyes"
    
    elif (a, b) == (1, 2):
        return "Ace Caught a Deuce"
    
    elif (a, b) == (2, 2):
        return "Little Joe from Kokomo"
    
    elif (a, b) in [(1, 4), (2, 3)]:
        return "Little Phoebe"
    
    elif (a, b) == (3, 3):
        return "Jimmy Hicks from the Sticks"
    
    elif (a, b) == (1, 6):
        return "Six Ace"
    
    elif (a, b) == (4, 4):
        return "Eighter from Decatur"
    
    elif (a, b) in [(3, 6), (4, 5)]:
        return "Nina from Pasadena"
    
    elif (a, b) == (5, 5):
        return "Puppy Paws"
    
    elif (a, b) == (5, 6):
        return "Six Five no Jive"
    
    elif (a, b) == (6, 6):
        return "Boxcars"

    # If it doesn't match any listed combo, 
    # just return and display no term.
    return "This roll has no term."

def main():

    # Main game loop, continues until the user decides to quit.
    while True:

        # Roll two dice and calculate the total.
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        total = d1 + d2

        # Display the results of the roll and the term.
        print(f"\nDie 1: {d1}")
        print(f"Die 2: {d2}")

        print(f"\nTotal: {total}")
        print(f"Term: {get_term(d1, d2)}")

        # Ask the user if they want to roll again.
        again = input("\nWould you like to roll again? (y/n): ")

        # If not, thank them for playing and exit the loop.
        if again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
