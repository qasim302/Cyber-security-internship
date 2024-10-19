import re


# Function to assess password strength
def assess_password_strength(password):
    # Criteria checks
    length_criteria = len(password) >= 8
    upper_criteria = any(char.isupper() for char in password)
    lower_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    # Initial score and feedback
    score = 0
    feedback = []

    # Check length
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if upper_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if lower_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digits
    if digit_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special characters
    if special_criteria:
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g. !@#$%^&*).")

    # Evaluate password strength based on score
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, feedback


# Main function to prompt the user for input
def main():
    print("-"*50)
    print("-->>Welcome to Nagra ")
    print("\t\tPassword Strength Checker")
    print("-"*50)

    # Get password input from the user
    password = input("Enter a password to check its strength: ")

    # Assess the password
    strength, feedback = assess_password_strength(password)

    # Display the results
    print(f"Password Strength: {strength}")

    if feedback:
        print("\nSuggestions for improvement:")
        for suggestion in feedback:
            print(f"- {suggestion}")


# Run the main function
if __name__ == "__main__":
    main()
