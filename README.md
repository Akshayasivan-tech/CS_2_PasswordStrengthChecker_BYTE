# Password Strength Checker

## About the Project

The Password Strength Checker is a Python-based cybersecurity project that evaluates the strength of a password.

It checks the password based on different security rules and classifies it as:

- Weak
- Moderate
- Strong

## Features

- Checks password length
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for numbers
- Checks for special characters
- Provides a strength score out of 5
- Displays the reasons for the result

## Password Rules

The program checks five conditions:

1. Password should contain at least 8 characters.
2. Password should contain an uppercase letter.
3. Password should contain a lowercase letter.
4. Password should contain a number.
5. Password should contain a special character.

Each satisfied condition gives 1 point.

### Strength Classification

| Score | Strength |
|------|----------|
| 0–2 | Weak |
| 3–4 | Moderate |
| 5 | Strong |

## How to Run

Make sure Python is installed.

Open the terminal in the project folder and run:

```bash
python password_checker.py