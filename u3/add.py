# 
# Extended List for Imports
# 

# Importing the list from `list.py`.
from list import items

# adding 5 new camping items to the existing list.
items.extend([
    "stove",
    "backpack",
    "sunscreen",
    "knife",
    "bug spray",
])

# Creating a new variable to hold the extended list.
extended_items = items

# Print the total number of items in the list after extending.
print("\nUpdated Total Items:", len(extended_items))

# Sort the list of items reversed alphabetically.
print("Updated Reversed Sorted Items:")

for extended_item in sorted(extended_items, reverse=True):
    print("-", extended_item)

# Non-Reverse sorted list, for testing purposes only.
# for extended_item in sorted(extended_items):
#     print("-", extended_item)
