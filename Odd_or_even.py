while True:
    try:
        # Prompt user to enter a number
        number = int(input("Enter a number to find out if it is odd or even: "))

        # Use the modulus operator to calculate the remainder of the number divided by 2
        result = number % 2

        # Check if the remainder is greater than 0
        if result > 0:
            # If the remainder is greater than 0, the number is odd
            print(str(number) + " is odd")
        else:
            # If the remainder is not greater than 0, the number is even
            print(str(number) + " is even")
    except ValueError:
        # If the user enters a non-numeric value, catch the ValueError and print an error message
        print("Error: Please enter a valid number.")
    except:
        # In case of any other error, catch the exception and print an error message
        print("Error: An unknown error occurred.")
