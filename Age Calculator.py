def check_age():
    age_input = input("Please enter your age: ")

    # Check if the input is a valid integer
    try:
        age = int(age_input)

        # Check if age is a valid positive integer
        if age < 0:
            print("Error: Age cannot be negative.")
            return

        # Check if age is even or odd
        if age % 2 == 0:
            print(f"Your age {age} is even.")
        else:
            print(f"Your age {age} is odd.")

    except ValueError:
        print("Error: Please enter a valid integer for age.")

# Run the program
check_age()