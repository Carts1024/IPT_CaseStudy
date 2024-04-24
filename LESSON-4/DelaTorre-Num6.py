""" Write a program that asks the user for an integer and 
creates a list that consists of the factors of that integer"""

try:
    integer = int(input("Enter an integer: "))
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
