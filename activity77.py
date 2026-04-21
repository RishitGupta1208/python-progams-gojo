import re

def check_password(password):
    if len(password) < 5:
        return "Step 1 Failed: Password must be at least 5 characters."
    if not any(char.isdigit() for char in password):
        return "Step 2 Failed: Add at least one number"
    if not any(char.isupper() for char in password):
        return "Step 3 Failed: Add at least one uppercase letter."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Step 4 Failed: Add a special character."

    return "Password passed Steps 1–4!"
while True:
    pwd = input("Enter your password: ")
    result = check_password(pwd)
    print(result)

    if "passed" in result:
        break