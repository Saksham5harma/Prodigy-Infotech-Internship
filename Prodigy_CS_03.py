#Password Complexity Checker
import re

def check_password_complexity(password):
    tips = []
    valid = True

    # Checking length
    if len(password) < 12:
        valid = False
        tips.append("Password should be at least 12 characters long.")

    # Checking presence of uppercase letter
    if not re.search(r"[A-Z]", password):
        valid = False
        tips.append("Password should contain at least one uppercase letter.")

    # Checking presence of lowercase letter
    if not re.search(r"[a-z]", password):
        valid = False
        tips.append("Password should contain at least one lowercase letter.")

    # Checking presence of number
    if not re.search(r"\d", password):
        valid = False
        tips.append("Password should contain at least one number.")

    # Checking presence of special character
    if not re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        valid = False
        tips.append("Password should contain at least one special character.")

    return {"valid": valid, "tips": tips}


password = input("Enter a password: ")
result = check_password_complexity(password)

if result["valid"]:
    print("Password is valid!")
else:
    print("Password is not valid. Here are some tips to strengthen it:")
    for tip in result["tips"]:
        print(tip)
