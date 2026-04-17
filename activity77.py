import re

def check_password(password):
    # Step 1: Length check
    if len(password) < 5:
        return "Step 1 Failed: Password must be at least 5 characters."

    # Step 2: Must contain a number
    if not any(char.isdigit() for char in password):
        return "Step 2 Failed: Add at least one number."

    # Step 3: Must contain uppercase letter
    if not any(char.isupper() for char in password):
        return "Step 3 Failed: Add at least one uppercase letter."

    # Step 4: Must contain special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Step 4 Failed: Add a special character."

    return "Password passed Steps 1–4!"

# Run the game
while True:
    pwd = input("Enter your password: ")
    result = check_password(pwd)
    print(result)

    if "passed" in result:
        break