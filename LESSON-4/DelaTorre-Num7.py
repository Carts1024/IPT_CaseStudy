""" Write a program that removes any repeated items from a list so that each item appears at most once.
For instance, the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0]. """

try:
    size = int(input("Enter the size of the list: "))

    #Ask user to input integers
    initialList = []
    print(f"Enter {size} integers:")
    for size in range(size):
        num = int(input())
        initialList.append(num)

    # Convert to set to remove duplicates easily
    finalList = (set(initialList))

    # Print the resulting list
    print("Original List:", initialList)
    print("List without duplicates:", finalList)

except ValueError:
    print("Invalid input. Please input an integer.")
