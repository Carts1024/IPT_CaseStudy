""" Starting with the list of the previous exercise, write Python statements to do the following: 
a. Append “banana” and 67 to the list. 
b. Insert the value “dog” at position 3. 
c. Insert the value 909 at the start of the list. 
d. Find the index of “hi”. 
e. Count the number of 67s in the list. 
f. Remove the first occurrence of 67 from the list. 
g. Remove False from the list using pop and index """

# Values from the list we made previously
list = [67, 62.9, 'hi', False, 8, 67, 'apple', 6.5]
print("List: ", list)
# A
list.append("banana")
list.append(67)
print("a. ", list)
# B
list.insert(3,"dog")
print("b. ", list)
# C 
list.insert(0, 909)
print("c. ", list)
# D
index = list.index("hi")
print("d. 'hi' is in index ", index)
# E
count = list.count(67)
print(f"e. There are '{count}' 67 in the list.")
# F
list.remove(67)
print("f. ", list)
# G
list.pop(4)
print("g. ", list)
