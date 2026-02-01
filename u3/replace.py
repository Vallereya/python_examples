# 
# Replace Item From List
# 

# Importing the list from `add.py`.
from add import items

# Replacing `stove` with `binoculars` in the existing list.
index = items.index("stove")
items[index] = "binoculars"
