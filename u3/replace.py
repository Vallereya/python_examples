# 
# Replace Item From List
# 

# Importing the list from `add.py`.
from add import extended_items

# Replacing `stove` with `binoculars` in the existing list.
# Find the index of `stove` and replace it.
index = extended_items.index("stove")
extended_items[index] = "binoculars"

# New variable to hold the updated list after replacement.
replaced_items = extended_items

# Print the total number of items in the list after replacement.
print("\nUpdated Total Items After Replacement:", len(replaced_items))

