while True:
    try:
        age = int(input("Enter your age: "))

        # Check for valid age range
        if age <= 0:
            print("Age must be greater than 0.")
            continue
        elif age > 120:
            print("Please enter a realistic age.")
            continue

        break  # valid input → exit loop

    except ValueError:
        print("Invalid input! Please enter a number only.")

# Check even or odd
if age % 2 == 0:
    print(f"Your age ({age}) is EVEN.")
else:
    print(f"Your age ({age}) is ODD.")