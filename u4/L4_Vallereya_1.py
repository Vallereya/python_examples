"""
    Program Name:   Deal Cards
    Author:         Vallereya
    Date:           2025-02-08
    Starter Code:   N/A
    Purpose:        This program will simulate a simple
                    dealing of cards. The user will specify
                    how many they want, and then the program
                    will randomly generate that many cards by
                    combining a random rank and suit.
"""

import random

# Card Values.
values = [
    "A",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "J",
    "Q",
    "K",
]

# Card Suits.
suits = [
    "H",
    "D",
    "C",
    "S",
]

# Get the number of cards to be dealt from the user.
dealt_cards = int(
    input("How many cards would you like to be dealt? ")
)

# Build a list of the cards to be dealt, no duplicates.
hand = []

while len(hand) < dealt_cards:

    # Get a random value and suit,
    # then combine them to make a card.
    value = random.choice(values)
    suit = random.choice(suits)
    card = value + suit

    # If the card is not already in the hand, add it.
    if card not in hand:
        hand.append(card)
    
# Print the hand of cards.
for card in hand:
    print(card)

# Print the number of cards that were dealt.
print("Total cards dealt:", dealt_cards)
