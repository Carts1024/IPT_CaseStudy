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
