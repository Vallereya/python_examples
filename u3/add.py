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

# Print the total number of items in the list after extending.
print("\nUpdated Total Items:", len(items))

# Sort the list of items reversed alphabetically.
print("Updated Reversed Sorted Items:")

for item in sorted(items, reverse=True):
    print("-", item)
