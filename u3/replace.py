# 
# Replace Item From List
# 

# Importing the list from `add.py`.
from add import extended_items

# Replacing `stove` with `binoculars` in the existing list.
# Find the index of `stove` and replace it.
index = extended_items.index("stove")
extended_items[index] = "binoculars"

# Sorting again the list after replacement.
extended_items.sort()

# Find the index of `binoculars` for later use.
new_index = extended_items.index("binoculars")

# Updated so that it can be run as a script, 
# when executed directly.
if __name__ == "__main__":

    # Print the total number of items in the list after replacement.
    print("Updated Total Items After Replacement:", len(extended_items))

    # Using Slice Notation to separate the list,
    # Print the updated list before replacement first.
    print("Items Before Replacement:")

    for item in extended_items[:new_index]:
        print("-", item)

    # Then printing the new_index item.
    print("\nNew Item:")

    for item in extended_items[new_index:new_index+1]:
        print("-", item)

    # And finally print the updated list after replacement.
    print("\nItems After Replacement:")

    for item in extended_items[new_index+1:]:
        print("-", item)
