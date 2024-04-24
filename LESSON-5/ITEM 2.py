""" WRITE A PROGRAM THAT WILL ASK USER TO INPUT A LIST OF INTEGER TUPLES.
ASK ALSO FOR ANOTHER INTEGER VALUE AND ASSIGN IT TO K. OUTPUT THE TUPLE THAT
ARE DIVISIBLE BY K."""

# Variable initialization
userTup = ()  # initializing empty tupke
listTup = list(userTup)  # converting tuple into a list
divTup = []  # empty tuple for elements divisible by k
elementCount = 1  # user input of number of elements
i = 1  # iteration variable
k = 0

# error handling
while (True):
    try:
        # user input of number of elements
        elementCount = int(input("Enter number of elements: "))
        # user input of divisor
        break
    except ValueError:  # if the wrong type was input
        print("Invalid input! Only Enter integer numbers!\n")

while (True):
    try:
        k = int(input("Enter an integer as divisor: "))
        break
    except ValueError:  # if the wrong type was input
        print("Invalid input! Only Enter integer numbers!\n")

while (True):
    try:
        # loop statement for updating the tuple/list
        while i <= elementCount:
            userInput = int(input("Enter elements [%i]: " % (i)))
            listTup.append(userInput)  # updating the list
            i += 1  # iteration
        break
    except ValueError:  # if the wrong type was input
        print("Invalid input! Only Enter integer numbers!\n")


# converting the list to tuple after updating
userTup = tuple(listTup)
print("List of tuples: ",  userTup)  # printing

# loop for elements divisible by k
for x in userTup:
    if x % k == 0:  # if there is no remainder, it is divisible by k
        divTup.append(x)  # updating the divTup tuple

# printing
print("List of tuples divisible by {}: ".format(k), divTup)
