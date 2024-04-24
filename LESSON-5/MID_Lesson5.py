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


def menu():  # Function for menu

    while True:
        os.system('cls')
        print('--------------------------------------------------------------')
        print('                     DICTIONARY METHODS')
        print('--------------------------------------------------------------\n')
        print('[1] Item #1')
        print('[2] Item #2')
        print('[3] Item #3')
        print('[4] Item #4')
        print('[5] Item #5')
        print('[6] Exit')

        choice = (input('\nEnter your choice: '))
        if choice != "":  # Checks if input is empty
            choice = int(choice)
            if choice >= 1 or choice <= 6:
                if choice == 1:
                    Item_1()  # Calls months Fction
                elif choice == 2:
                    Item_2()  # Calls Alphabetical Function
                elif choice == 3:
                    Item_3()  # Calls days_31 Function
                elif choice == 4:
                    Item_4()  # Calls Sorting Function
                elif choice == 5:
                    Item_5()
                elif choice == 6:
                    return  # Exit
            else:
                print("\nEnter valid choice")
        else:
            print("Enter valid choice")


def Item_1():
    os.system('cls')
    print(
        '----------------------------------------------------------------------------------------------------------------------------')
    print(
        '                     WRITE A PYTHON PROGRAM TO CREATE A LIST OF TUPLES HAVING FIRST ELEMENT AS THE\n       NUMBER AND SECOND ELEMENT AS THE SQUARE OF THE NUMBER. INPUT: LIST = [1, 2, 3] OUTPUT: [(1, 1), (2, 4), (3, 9)]')
    print(
        '----------------------------------------------------------------------------------------------------------------------------\n')
    # Initialize tuple
    squared = ()

    # Inputs in list
    list = [1, 2, 3]

    # List for squared numbers
    sq_list = []

    # Loop for squaring numbers
    for i in list:
        sq = i * i
        squared = (i, sq)
        # Adding squared numbers tuple to the list
        sq_list.append(squared)
        del squared

    # Print Results
    print("Input:", list)
    print("Squared Numbers: ", sq_list)
    input('')
    return  # Back to menu


def Item_2():
    os.system('cls')
    print(
        '----------------------------------------------------------------------------------------------------------------------------')
    print(
        '                      WRITE A PROGRAM THAT WILL ASK USER TO INPUT A LIST OF INTEGER TUPLES.\n                      ASK ALSO FOR ANOTHER INTEGER VALUE AND ASSIGN IT TO K.\n                      OUTPUT THE TUPLE THAT ARE DIVISIBLE BY K.')
    print(
        '----------------------------------------------------------------------------------------------------------------------------\n')

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
            # loop statement for updating the tuple/list
            while i <= elementCount:
                userInput = int(input("Enter elements [%i]: " % (i)))
                listTup.append(userInput)  # updating the list
                i += 1  # iteration
            break
        except ValueError:  # if the wrong type was input
            print("Invalid input! Only Enter integer numbers!\n")

    while (True):
        try:
            k = int(input("Enter an integer as divisor: "))
            break
        except ValueError:  # if the wrong type was input
            print("Invalid input! Only Enter integer numbers!\n")

    # converting the list to tuple after updating
    userTup = tuple(listTup)
    print("List of tuples: ", userTup)  # printing

    # loop for elements divisible by k
    for x in userTup:
        if x % k == 0:  # if there is no remainder, it is divisible by k
            divTup.append(x)  # updating the divTup tuple

    # printing
    print("List of tuples divisible by {}: ".format(k), divTup)
    input('')
    return  # Back to menu


def Item_3():
    # Initialize Disctionary for months and days
    days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31,
            'September': 30, 'October': 31, 'November': 30, 'December': 31}
    days_display = days.items()
    os.system('cls')
    print(
        '----------------------------------------------------------------------------------------------------------------------------')
    print('                      HERE IS A DICTIONARY OF THE DAYS IN THE MONTHS OF THE YEAR: \n')
    for keys, value in days_display:
        print('                      ', keys, ' : ', value)
    print(
        '----------------------------------------------------------------------------------------------------------------------------\n')
    input('')

    def menu_Item3():  # Function for menu
        while True:
            try:
                os.system('cls')
                print('--------------------------------------------------------------')
                print('                     DICTIONARY METHODS')
                print('--------------------------------------------------------------\n')
                print('[1] How many days are the in a month?')
                print('[2] Print months in alphabetical order')
                print('[3] Print all months with 31 days')
                print('[4] Print (key-value) pairs sorted by number of days')
                print('[5] Exit')
                choice = int(input('\nEnter your choice: '))
                if 1 <= choice <= 5:  # Corrected condition
                    if choice == 1:
                        Months()  # Calls months Function
                    elif choice == 2:
                        alphabetical()  # Calls Alphabetical Function
                    elif choice == 3:
                        days_31()  # Calls days_31 Function
                    elif choice == 4:
                        sorted_days()  # Calls Sorting Function
                    elif choice == 5:
                        break  # Exit
                else:
                    print("\nEnter valid choice")
            except ValueError:  # if the wrong type was input
                print("Invalid input! Only Enter integer numbers!\n")

    def Months():  # Function for asking the user to enter a month name and use the dictionary to tell them how many days are in the month.
        os.system('cls')
        while True:
            Month = input("Enter a month name to know how many days are there in that month: ")
            if len(Month) != 0:  # Checks if the user entered a value
                Month = Month[0].upper() + Month[1:]
                if Month in days:  # Checks if the input is in the dictionary
                    break
                else:
                    print("Enter a valid input")
            else:
                print("Enter a valid input")
        print(days.get(Month))
        input('')
        return  # Back to the menu

    def alphabetical():  # Function for printing out all of the keys in alphabetical order.

        os.system('cls')
        sorted_keys = sorted(days.keys())
        for key in sorted_keys:
            print(key)
        input('')
        return  # Back to the menu

    def days_31():  # Function for printing out all of the months with 31 days.
        os.system('cls')
        print('MONTHS WITH 31 DAYS: \n')
        for key in days:
            if days[key] == 31:
                print(key)
        input('')
        return  # Back to the menu

    def sorted_days():  # Function for printing out the (key-value) pairs sorted by the number of days in each month
        os.system('cls')
        sorted_days = sorted(days.items(), key=lambda x: x[1], reverse=True)
        for key, value in sorted_days:
            print(key, ':', value)
        input('')
        return  # Back to the menu

    menu_Item3()
    return


def Item_4():
    os.system('cls')
    print(
        '----------------------------------------------------------------------------------------------------------------------------')
    print(
        '           WRITE A PROGRAM THAT REPEATEDLY ASKS THE USER TO ENTER PRODUCT NAMES AND PRICES.\n           STORE ALL OF THESE IN A DICTIONARY WHOSE KEYS ARE THE PRODUCT NAMES AND WHOSE VALUES ARE THE PRICES.\n           WHEN THE USER IS DONE ENTERING PRODUCTS AND PRICES, ALLOW THEM TO REPEATEDLY ENTER A PRODUCT NAME AND\n           PRINT THE CORRESPONDING PRICE OR A MESSAGE IF THE PRODUCT IS NOT IN THE DICTIONARY.')
    print(
        '----------------------------------------------------------------------------------------------------------------------------\n')
    input('')
    # Sample dictionary
    products = {}

    def inputf():
        input_product = str(input('Enter a product: '))
        input_product = input_product[0].upper() + input_product[1:]
        input_price = float(input('Enter a price: '))
        products[input_product] = input_price

    def repeat():
        choice = (str(input('Do you want to enter again? (Press Y to continue): '))).upper()
        return choice

    def ask():
        choice = 'Y'
        while (choice == 'Y'):
            os.system('cls')
            find_product = input('Enter product you want to check price: ')
            find_product = find_product[0].upper() + find_product[1:]
            if find_product in products:
                print('The price of', find_product, 'is', products.get(find_product))
            else:
                print('The item is not in the dictionary')
            choice = repeat()

    os.system('cls')
    choice = 'Y'
    while (choice == 'Y'):
        inputf()
        choice = repeat()
    print(products)
    ask()
    input('')
    return


def Item_5():
    # Dictionary with usernames and passwords
    systemUsers = {
        'Mae': "Loraine",
        "Ymata": "Dela Torre",
        "Crystal": "Lyn",
        "Rubio": "Danga",
        "Lei": "Ann",
        "Marribay": "Soreto",
        "Carl": "Aldrey",
        "Daulo": "Bergado",
        "Clarisse": "Irish",
        "Jotojot": "Paller"
    }
    os.system('cls')
    print(
        '--------------------------------------------------------------------------------------------------------------------------------------------------')
    print(
        '     WRITE A PROGRAM THAT USES A DICTIONARY THAT CONTAINS TEN USER NAMES AND PASSWORDS.\n     THE PROGRAM SHOULD ASK THE USER TO ENTER THEIR USERNAME AND PASSWORD.\n     IF THE USERNAME IS NOT IN THE DICTIONARY, THE PROGRAM SHOULD INDICATE THAT THE PERSON IS NOT A VALID USER OF THE SYSTEM.\n     IF THE USERNAME IS IN THE DICTIONARY, BUT THE USER DOES NOT ENTER THE RIGHT PASSWORD, THE PROGRAM SHOULD SAY THAT THE PASSWORD IS INVALID.\n     IF THE PASSWORD IS CORRECT, THEN THE PROGRAM SHOULD TELL THE USER THAT THEY ARE NOW LOGGED IN TO THE SYSTEM.')
    print(
        '--------------------------------------------------------------------------------------------------------------------------------------------------\n')
    input('')
    choice = 'Y'
    while (choice == 'Y'):

        os.system('cls')
        users = systemUsers.items()
        for key, value in users:
            print('--------------------------------------------------------------')
            print('           USERNAME: ', key, '     PASSWORD: ', value)
            print('--------------------------------------------------------------')

        # Input username
        username = (input("Enter your username: "))

        # Condition to check if the inputs match in the dictionary
        if username in systemUsers:  # Check if the username exist
            # Input Password
            while True:
                password = input("Enter your password: ")
                if systemUsers[username] == password:  # When inputs match
                    print("\nYou have logged in successfully.")
                    print(f"Hello, {username}!")
                    choice = input('Do you want to try again? (Press Y to continue): ').upper()
                    break
                else:  # When the user input a wrong password
                    print("\nInvalid password.")
                    continue
        else:  # When the username does not exist
            print(f"\nSorry, '{username}' is not a valid user.")
            continue
    return


if __name__ == "__main__":
    os.system('cls')
    start()
    menu()
