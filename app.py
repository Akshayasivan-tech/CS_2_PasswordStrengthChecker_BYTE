import streamlit as st
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


st.title("Password Strength Checker")
st.write("Check the strength of your password based on five security criteria.")

password = st.text_input(
    "Enter your password:",
    type="password"
)

if st.button("Check Password"):
    if password:
        score, strength, reasons = check_password(password)

        st.subheader(f"Password Strength: {strength}")
        st.write(f"**Score: {score}/5**")

        st.write("### Details")

        for reason in reasons:
            st.write(f"✓ {reason}")
    else:
        st.warning("Please enter a password.")
