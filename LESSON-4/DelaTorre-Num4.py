""" Write a program that asks the user to enter size of list and input a list of integers. Do the following:’ 
a. Print the sum of items in the list. 
b. Print the last item in the list. 
c. Print the list in reverse order. 
d. Print Yes if the list contains a 5 and No otherwise. 
e. Print how many integers in the list are less than 5. 
f. Remove the first and last items from the list, sort the remaining items, and print the result."""

# Enter size of list
size = int(input("Enter the size of the list: "))

# Input integers in the list
integers = []
print(f"Enter {size} integers:")
for size in range(size):
    num = int(input())
    integers.append(num)

# a. Print the sum of items in the list
print("Sum:", sum(integers))

# b. Print the last item in the list
print("Last:", integers[-1])

# c. Print the list in reverse order
print("List in reverse order:", integers[::-1])

# d. Print Yes if the list contains a 5 and No otherwise
if 5 in integers:
    print("Yes")
else:
    print("No")

# e. Print how many integers in the list are less than 5
lessThan5Count = 0
for num in integers:
    if num < 5:
        lessThan5Count += 1
print("Number of integers less than 5:", lessThan5Count)

# f. Remove the first and last items from the list, sort the remaining items, and print the result
if len(integers) > 2:
    integers.pop(0)  # Remove the first item
    integers.pop(-1)  # Remove the last item
    integers.sort()  # Sort the remaining items
    print("After removing first and last items and sorting:", integers)
else:
    print("Items cannot be removed because the list is too short. Otherwise, the list will be empty.")
