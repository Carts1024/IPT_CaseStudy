"""Create a list with the following six items: 67, 62.9, “hi”, False, 8, 67, ‘apple’, 6.5. 
Begin with the empty list shown below, and add 8 statements to add each item, one per item.
The first four statements should use the append method to append the item to the list,
and the last four statements should use concatenation"""

# Create an empty list
list = []

# Add values to list using append
list.append(67)
list.append(62.9)
list.append("hi")
list.append(False)

# Add values to list using concatenation
list += [8, 67, 'apple', 6.5]

print(list)
