import os

def start():  # Main (Function 1)

    print('--------------------------------------------------------------')
    print('               WELCOME TO DICTIONARY METHODS BY GROUP 6')
    print('                              MEMBERS:\n')
    print('                        BERGADO,CARL ALDREY')
    print('                        DANGA, CRYSTALYN')
    print('                        DELA TORRE, MAE LORAINE')
    print('                        PALLER, CLARISSE IRISH')
    print('                        SORETO, LEI ANN\n')
    input(
        '                       PRESS ENTER TO CONTINUE\n--------------------------------------------------------------')
    os.system('cls')


def First_Number():
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
    input('')
    return


def Second_Number():
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
    input('')
    return

def Third_Number():
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
    input('')
    return

def Fifth_Number():
    mylist = []

    while True:
        try:
            num_list = int(input("How many elements do you want in the list?: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    while True:
        try:
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
            if element_count == 1:
                mylist.pop(0)
            else:
                mylist.pop(0)
                mylist.pop(-1)
            print("Letter f: Remove first and last item = ", mylist)
            mylist.sort()
            print("Letter f: Sorted list = ", mylist)
            input('')
            return
        except ValueError:
            print("Invalid input.")
            input('')
            continue

def Sixth_Number():
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
    input('')
    return

def Seventh_Number():
    while True:
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
                input('')
                return
        except ValueError:
            print("Invalid input. Please enter an integer.")
            input('')
            continue

def Eight_Number():
    while True:
        try:
            size = int(input("\nEnter the size of the list: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

    while True:
        try:
            # Ask user to input integers
            initialList = []
            print(f"Enter {size} integers:")
            for _ in range(size):
                num = int(input("Enter values: "))
                initialList.append(num)

            # Convert to set to remove duplicates easily
            finalList = (set(initialList))

            # Print the resulting list
            print("Original List:", initialList)
            print("List without duplicates:", finalList)
            input('')
            return
        except ValueError:
            print("Invalid input. Please input an integer.")
            continue

def RunProgram():
    while True:
        try:
            os.system('cls')
            print("===============================================================================================")
            print("\t\t\t\tWELCOME TO LESSON 4: LIST")
            print("===============================================================================================")
            print("CHOOSE A NUMBER TO BE VIEWED")
            print("[1] Problem 1")
            print("[2] Problem 2")
            print("[3] Problem 3 and 4")
            print("[5] Problem 5")
            print("[6] Problem 6")
            print("[7] Problem 7")
            print("[8] Problem 8")
            print("[9] Exit")

            userChoice = int(input("Enter your choice: "))

            if 1 <= userChoice <= 9:
                if userChoice == 1:
                    First_Number()
                elif userChoice == 2:
                    Second_Number()
                elif userChoice == 3:
                    Third_Number()
                elif userChoice == 4:
                    print(f"{userChoice} is not available in the menu. Please enter another number.")
                    input('')
                    continue
                elif userChoice == 5:
                    Fifth_Number()
                elif userChoice == 6:
                    Sixth_Number()
                elif userChoice == 7:
                    Seventh_Number()
                elif userChoice == 8:
                    Eight_Number()
                elif userChoice == 9:
                    print("End of program. Thank you!")
                    break
            else:
                print("\nInvalid input! Choose what is only available!")
                input('')
        except ValueError:
            print("Invalid input. Please choose between 1-9.")
            input('')

start()
RunProgram()
