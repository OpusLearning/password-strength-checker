import re

def check_password_strength(password):
    # Criteria for password strength
    length = len(password) >= 10
    digit = re.search(r"\d", password) is not None
    uppercase = re.search(r"[A-Z]", password) is not None
    lowercase = re.search(r"[a-z]", password) is not None
    special_char = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    strength = length and digit and uppercase and lowercase and special_char
    return "Strong" if strength else "Weak"

# User input
user_password = input("Enter your password to check if it is worthy: ")
strength = check_password_strength(user_password)
print(f"Your password is: {strength}")
