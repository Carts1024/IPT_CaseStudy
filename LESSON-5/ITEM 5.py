"""Write a program that uses a dictionary that contains ten user names and passwords.
The program should ask the user to enter their username and password.
If the username is not in the dictionary, the program should indicate that 
the person is not a valid user of the system. If the username is in the dictionary, 
but the user does not enter the right password, the program should say that the password is invalid.
If the password is correct, then the program should tell the user that they are now logged in to the system."""


def SystemLogin():
    usernameInput = input("Enter username: ")
    passwordInput = input("Enter password: ")
    
    accounts = {
        'Clarisse': 'Paller',
        'Mae': 'Dela Torre',
        'Crystal': 'Danga',
        'Lei': 'Soreto',
        'Carl': 'Bergado',
        'Loraine': 'Ymata',
        'Lyn': 'Rubio',
        'Irish': 'Jotojot',
        'Ann': 'Soreto',
        'Aldrey': 'Daulo'
    }

    if usernameInput in accounts:
        if passwordInput == accounts[usernameInput]:
            print("You are now logged in to the system.")
        else:
            print("Invalid password.")
    else: 
        print("Username is not a valid user of the system.")
        SystemLogin()
    
SystemLogin()

# --- SI RAINE TO HEHE GAWA KO DITO SA BABA

# Dictionary with usernames and passwords
systemUsers = {
    "Mae": "Loraine",
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

# Input username and password
username = input("Enter your username: ")
password = input("Enter your password: ")

# Condition to check if the inputs match in the dictionary
if username in systemUsers:  # Check if the username exist
    if systemUsers[username] == password:  # When inputs match
        print("\nYou have logged in successfully.")
        print(f"Hello, {username}!")
    else:  # When the user input a wrong password
        print("\nInvalid password.")
else:  # When the username does not exist
    print(f"\nSorry, '{username}' is not a valid user.")
