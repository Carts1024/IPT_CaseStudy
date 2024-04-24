def SystemLogin():
    usernameInput = input("Enter username: ")
    passwordInput = input("Enter password: ")
    
    accounts = {
        'user1': 'password1',
        'user2': 'password2',
        'user3': 'password3',
        'user4': 'password4',
        'user5': 'password5',
        'user6': 'password6',
        'user7': 'password7',
        'user8': 'password8',
        'user9': 'password9',
        'user10': 'password10'
    }

    if usernameInput in accounts:
        if passwordInput == accounts[usernameInput]:
            print("You are now logged in to the system.")
        else:
            print("Invalid password.")
    else: 
        print("Username is not a valid user of the system.")
    

SystemLogin()
