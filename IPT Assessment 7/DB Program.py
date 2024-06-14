import sqlite3
import os

def start():  # Function to display the welcome message (Function 1)
    print('--------------------------------------------------------------')
    print('               WELCOME TO DATABASE CONNECTIVITY BY GROUP 6')
    print('                              MEMBERS:\n')
    print('                        BERGADO, CARL ALDREY')
    print('                        DANGA, CRYSTALYN')
    print('                        DELA TORRE, MAE LORAINE')
    print('                        PALLER, CLARISSE IRISH')
    print('                        SORETO, LEI ANN\n')
    input('                       PRESS ENTER TO CONTINUE\n--------------------------------------------------------------')
    os.system('cls')  # Clear screen for cleaner interface

def menu():  # Function for menu
    while True:
        os.system('cls')  # Clear screen
        print('--------------------------------------------------------------')
        print('                     DATABASE CONNECTIVITY')
        print('--------------------------------------------------------------\n')
        print('[A] ADD')
        print('[E] EDIT')
        print('[L] LIST')
        print('[R] REMOVE')
        print('[Q] QUIT')

        choice = input('\nEnter your choice: ')
        if choice:  # Check if input is not empty
            choice = choice.upper()  # Convert choice to uppercase

            if choice in ["A", "E", "L", "R", "Q"]:
                if choice == "A":
                    add()  # Call add function for ADD functionality
                elif choice == "E":
                    edit()  # Call edit function for EDIT functionality
                elif choice == "L":
                    initialize()  # Call initialize function to list bookmarks
                elif choice == "R":
                    remove()  # Call remove function for REMOVE functionality
                elif choice == "Q":
                    exit()  # Exit the program
            else:
                print("\nEnter a valid choice")
        else:
            print("Enter a valid choice")

def initialize():  # Function to list all bookmarks
    # Connect to the SQLite database
    conn = sqlite3.connect('Bookmarks.db')

    # Define the query to fetch data
    view = "SELECT * FROM Bookmark"
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(view)
        rows = cursor.fetchall()

        # Print each row in the custom format
        for i in rows:
            id, title, url = i
            print(f"({id}) {title}........{url}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
        input('\nPress ENTER to return to the menu')  # Pause before returning to the menu
        return

def edit():  # Function to edit a bookmark
    numbook = int(input("Number of bookmark to edit: "))
    # Connect to the SQLite database
    conn = sqlite3.connect('Bookmarks.db')

    # Define the query to fetch data
    sql = f"SELECT * FROM Bookmark WHERE Bk_ID ={numbook} "
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(sql)
        rows = cursor.fetchone()

        if rows:
            id, title, url = rows
            newUrl = input(f"URL [{url}]: ")
            newTitle = input(f"Title [{title}]: ")
            updateScript = f"UPDATE Bookmark SET Title = '{newTitle}', URL = '{newUrl}' WHERE Bk_ID = {numbook}"
            cursor.execute(updateScript)
            conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
        input('\nPress ENTER to return to the menu')  # Pause before returning to the menu
        return

def add():  # Function to add a new bookmark
    addTitle = input("Enter bookmark title: ")
    addURL = input("Enter bookmark url: ")
    # Connect to the SQLite database
    conn = sqlite3.connect('Bookmarks.db')

    # Define the query to insert data
    sql = f"INSERT INTO Bookmark (Title, URL) VALUES ('{addTitle}','{addURL}')"
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(sql)
        conn.commit()
        print("Bookmark added successfully")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
        input('\nPress ENTER to return to the menu')  # Pause before returning to the menu
        return

def remove():  # Function to remove a bookmark
    # Connect to the SQLite database
    conn = sqlite3.connect('Bookmarks.db')

    # Define the query to fetch data
    view = "SELECT * FROM Bookmark"
    cursor = conn.cursor()

    try:
        # Execute the query
        cursor.execute(view)
        rows = cursor.fetchall()

        # Print each row in the custom format
        for i in rows:
            id, title, url = i
            print(f"({id}) {title}........{url}")

        delID = input("\nWhat bookmark do you want to delete(Bookmark Number)?: ")
        delete = f"DELETE FROM Bookmark WHERE Bk_ID = {delID}"
        cursor.execute(delete)
        conn.commit()
        print("Bookmark removed successfully")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
        input('\nPress ENTER to return to the menu')  # Pause before returning to the menu
        return

if __name__ == "__main__":
    start()  # Call the start function to display the welcome message
    menu()  # Call the menu function to start the main menu loop
