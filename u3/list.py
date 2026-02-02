# 
# Initial List
# 

# List of camping items.
items = [
    "tent poles",
    "sleeping bag",
    "flashlight",
    "first aid kit",
    "water",
    "food",
    "matches",
    "map",
    "compass",
    "clothing",
]

# Updated so that it can be run as a script, 
# when executed directly.
if __name__ == "__main__":

    # Print the total number of items in the list.
    print("Initial Total Items:", len(items))

    # Sort the list of items alphabetically.
    print("Initial Sorted Items:")

    for item in sorted(items):
        print("-", item)
