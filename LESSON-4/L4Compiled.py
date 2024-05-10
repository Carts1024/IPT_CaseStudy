import os


def First_Number():
    os.system('cls')

    x = [1, 2, 3, 4, 5]
    y = [11, 12, 13, 14, 15]
    z = [21, 22, 23, 24, 25]

    prod = 0
    prodList = []
    for i in x:
        prod = 3 * i
        prodList.append(prod)
        prod = 0
    print("a. 3*y = ", prodList)

    sum = 0
    sumList = []
    for i in range(len(x)):
        sum = x[i] + y[i]
        sumList.append(sum)
    print("b. x+y = ", sumList)

    subtract = 9
    subList = []
    for i in range(len(x)):
        subtract = x[i] - y[i]
        subList.append(subtract)
    print("c. x-y = ", subList)

    print("d.", x[1])
    print("e.", x[0])
    print("f.", x[-1])
    print("g.", x[:])
    print("h.", x[2:4])
    print("i.", x[1:4:2])
    print("j.", x[:2])
    print("k.", x[::2])
    x[3] = 8
    print("l. x[3] = 8 = ", x)

    return


def Second_Number():
    os.system('cls')
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


def Third_Number():
    os.system('cls')
    mylist = []

    mylist.append(67)
    mylist.append(62.9)
    mylist.append("hi")
    mylist.append(False)

    mylist = mylist + [8]
    mylist = mylist + [67]
    mylist = mylist + ["apple"]
    mylist = mylist + [6.5]

    print("\nOriginal List: ", mylist)

    mylist.append("banana")
    mylist.append(67)
    print("Letter a: ", mylist)

    mylist.insert(2, "dog")
    print("Letter b: ", mylist)

    mylist.insert(0, 909)
    print("Letter c: ", mylist)

    print("Letter d: ", mylist.index("hi"))

    print("Letter e: ", mylist.count(67))

    mylist.remove(67)
    print("Letter f: ", mylist)

    index = mylist.index(False)
    mylist.pop(index)
    print("Letter g: ", mylist)


def Fifth_Number():
    os.system('cls')
    mylist = []

    num_list = int(input("How many elements do you want in the list?: "))

    sum = 0
    for _ in range(num_list):
        element = int(input("Enter an element: "))
        sum = sum + element
        mylist.append(element)
    print("Letter a: Sum of items = ", sum)

    print("Letter b: Last item on the list ", mylist[-1])

    mylist.reverse()
    print("Letter c: Items in reversed order = ", mylist)

    if 5 in mylist:
        print("Letter d: 'Yes'")
    else:
        print("Letter d: 'No'")

    element_count = 0
    for _ in mylist:
        if _ < 5:
            element_count += 1

    print("Letter e: ", element_count)
    mylist.pop(0)
    mylist.pop(-1)
    print("Letter f: Remove first and last item = ", mylist)
    mylist.sort()
    print("Letter f: Sorted list = ", mylist)


def Sixth_Number():
    os.system('cls')
    f = [8, 9, 10]

    f[1] = 17
    print("Letter a: ", f)

    f.extend([4, 5, 6])
    print("Letter b: ", f)

    f.pop(0)
    print("Letter c: ", f)

    f.sort()
    print("Letter d: ", f)

    f = f*2
    f.insert(3, 25)
    print("Letter e: ", f)


def Seventh_Number():
    os.system('cls')
    try:
        integer = int(input("\nEnter an integer: "))
        factors = []

        # Evaluate the input
        if integer == 0:  # When integer is 0
            print("Zero has no common factors with any other number except for zero.")
            print("Any number divided by zero is undefined.")
        elif integer < 0:  # When integer is a negative number
            print("Invalid input. Please enter a positive integer.")
        else:
            # Find factors of the integer
            for i in range(1, integer + 1):
                if integer % i == 0:
                    factors.append(i)  # Store to the list
            # Print the list of factors
            print(f"Factors of {integer}:", factors)
    except ValueError:
        print("Invalid input. Please enter an integer.")


def Eight_Number():
    os.system('cls')
    try:
        size = int(input("\nEnter the size of the list: "))

        # Ask user to input integers
        initialList = []
        print(f"Enter {size} integers:")
        for size in range(size):
            num = int(input("Enter values: "))
            initialList.append(num)

        # Convert to set to remove duplicates easily
        finalList = (set(initialList))

        # Print the resulting list
        print("Original List:", initialList)
        print("List without duplicates:", finalList)

    except ValueError:
        print("Invalid input. Please input an integer.")


def RunProgram():
    while True:
        os.system('cls')
        print("CHOOSE A NUMBER TO BE VIEWED")
        print("[1] Problem 1")
        print("[2] Problem 2")
        print("[3] Problem 3 and 4")
        print("[5] Problem 5")
        print("[6] Problem 6")
        print("[7] Problem 7")
        print("[8] Problem 8")

        try:
            userChoice = int(input("Enter your choice: "))
            if userChoice == 1:
                print("\nExecuting Problem 1...\n")
                First_Number()
            elif userChoice == 2:
                print("\nExecuting Problem 2...\n")
                Second_Number()
            elif userChoice == 3:
                print("\nExecuting Problem 3 and 4...\n")
                Third_Number()
            elif userChoice == 5:
                print("\nExecuting Problem 5...\n")
                Fifth_Number()
            elif userChoice == 6:
                print("\nExecuting Problem 6...\n")
                Sixth_Number()
            elif userChoice == 7:
                print("\nExecuting Problem 7...\n")
                Seventh_Number()
            elif userChoice == 8:
                print("\nExecuting Problem 8...\n")
                Eight_Number()
            else:
                print("\nInvalid choice! Please choose a number from the menu.")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

        input("\nPress Enter to continue...")


def start():  # Main (Function 1)

    print('--------------------------------------------------------------')
    print('               WELCOME TO LIST METHODS BY GROUP 6')
    print('                              MEMBERS:\n')
    print('                        BERGADO,CARL ALDREY')
    print('                        DANGA, CRYSTALYN')
    print('                        DELA TORRE, MAE LORAINE')
    print('                        PALLER, CLARISSE IRISH')
    print('                        SORETO, LEI ANN\n')
    input(
        '                       PRESS ENTER TO CONTINUE\n--------------------------------------------------------------')
    os.system('cls')


start()
RunProgram()
