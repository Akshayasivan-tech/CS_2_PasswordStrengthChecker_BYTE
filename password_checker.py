import string

def check_password(password):
    score = 0
    reasons = []

    # Length check
    if len(password) >= 8:
        score += 1
        reasons.append("At least 8 characters")
    else:
        reasons.append("Less than 8 characters")

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
        reasons.append("Contains uppercase letter")

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1
        reasons.append("Contains lowercase letter")

    # Number check
    if any(char.isdigit() for char in password):
        score += 1
        reasons.append("Contains number")

    # Special character check
    if any(char in string.punctuation for char in password):
        score += 1
        reasons.append("Contains special character")

    # Strength category
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, reasons


password = input("Enter your password: ")

score, strength, reasons = check_password(password)

print("\nPassword Strength:", strength)
print("Score:", score, "/ 5")
print("\nDetails:")

for reason in reasons:
    print("-", reason)