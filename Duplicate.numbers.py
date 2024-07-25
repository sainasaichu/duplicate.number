# Define three sample lists
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
list3 = [6, 7, 8, 9, 10, 11]

# Convert lists to sets
set1 = set(list1)
set2 = set(list2)
set3 = set(list3)

# Find the intersection of the three sets to get the common elements
duplicates = set1 & set2 & set3

# Convert the result back to a list (optional)
duplicates_list = list(duplicates)

# Print the duplicates
print("Duplicates across the three lists are:", duplicates_list)
