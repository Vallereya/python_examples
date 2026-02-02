# 
# Remove Item From List
# 

from replace import replaced_items

# Removing `binoculars` from the existing list, if it exists.
if "binoculars" in replaced_items:
    replaced_items.remove("binoculars")

# Creating a new variable to hold the final list.
final_items = replaced_items

# No need to sort the final list again, so I can just print it.
# Since, this is the last operation in the sequence,
# this will be the final output/main result.
if __name__ == "__main__":

    # Print the final sorted list of items.
    print("Final Sorted Items After Removal:")

    for item in sorted(final_items):
        print("-", item)

    # Print the total number of items in the list after removal, using a f-string.
    print(f"Total items being brought on the camping trip: {len(final_items)}")
