""" Start with the list [8,9,10]. Do the following: 
a. Set the second entry (index 1) to 17 
b. Add 4, 5, and 6 to the end of the list 
c. Remove the first entry from the list 
d. Sort the list 
e. Double the list 
f. Insert 25 at index 3 
The final list should equal [4,5,6,25,10,17,4,5,6,10,17] """

list = [8, 9, 10]
print("Initial List: ", list)
# A
list.insert(1, 17)
print("a. ", list)
# B
list += 4, 5, 6
print("b. ", list)
# C
list.pop(0)
print("c. ", list)
# D
list.sort()
print("d. ", list)
# E
list = 2 * list
print("e. ", list)
# F
list.insert(3, 25)
print("Final list: ", list)
