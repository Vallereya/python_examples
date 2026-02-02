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

# Print the total number of items in the list after replacement.
print("Updated Total Items After Replacement:", len(extended_items))

