def getUserInput():
    usernameInput = input("Enter username: ")
    passwordInput = input("Enter password: ")
    usernames = {
        "username1" : "Mae",
        "username2" : "Loraine",
        "username3" : "Crystal",
        "username4" : "Lyn",
        "username5" : "Clarisse",
        "username6" : "Irish",
        "username7" : "Lei",
        "username8" : "Ann",
        "username9" : "Carl",
        "username10" : "Aldrey"
    }
    passwords = {
        "password1" : "Ymata",
        "password2" : "Dela Torre",
        "password3" : "Rubio",
        "password4" : "Danga",
        "password5" : "Jotojot",
        "password6" : "Paller",
        "password7" : "Marribay",
        "password8" : "Soreto",
        "password9" : "Daulo",
        "password10" : "Bergado"
    }

    if usernameInput in usernames.values():
        if usernameInput == "Mae" and passwordInput == "Ymata":
            print("You are now logged in to the System.")
                
        elif usernameInput == "Loraine" and passwordInput == "Dela Torre":
            print("You are now logged in to the System.")
        
        elif usernameInput == "Crystal" and passwordInput == "Rubio":
            print("You are now logged in to the System.")

        elif usernameInput == "Lyn" and passwordInput == "Danga":
            print("You are now logged in to the System.")

        elif usernameInput == "Clarisse" and passwordInput == "Jotojot":
            print("You are now logged in to the System.")

        elif usernameInput == "Irish" and passwordInput == "Paller":
            print("You are now logged in to the System.")

        elif usernameInput == "Lei" and passwordInput == "Marribay":
            print("You are now logged in to the System.")

        elif usernameInput == "Ann" and passwordInput == "Soreto":
            print("You are now logged in to the System.")

        elif usernameInput == "Carl" and passwordInput == "Daulo":
            print("You are now logged in to the System.")

        elif usernameInput == "Aldrey" and passwordInput == "Bergado":
            print("You are now logged in to the System.")
            
        else:
                print("Incorrect Password.")
    else:
        print("Username not found.")
        getUserInput

getUserInput()
