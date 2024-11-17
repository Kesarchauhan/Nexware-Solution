import random
import string
import pyperclip

# Function to generate a password
def generate_password(length, complexity, avoid_ambiguous):
    characters = string.ascii_lowercase
    if complexity >= 2:
        characters += string.ascii_uppercase + string.digits
    if complexity == 3:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/|"
    
    # Remove ambiguous characters if option selected
    if avoid_ambiguous:
        ambiguous_chars = "lI1O0"
        characters = ''.join(ch for ch in characters if ch not in ambiguous_chars)
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to assess password strength
def assess_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 10:
        return "Moderate"
    else:
        return "Strong"

# Main program
def password_generator():
    history = []
    print("Welcome to the Enhanced Password Generator!")
    
    while True:
        # Get user input
        try:
            length = int(input("Enter the desired password length (minimum 5): "))
            if length < 5:
                print("Password length must be at least 5 characters. Try again.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        print("\nSelect complexity level:")
        print("1. Basic (Lowercase only)")
        print("2. Intermediate (Lowercase, Uppercase, Digits)")
        print("3. Advanced (Lowercase, Uppercase, Digits, Special Characters)")
        
        try:
            complexity = int(input("Enter your choice (1-3): "))
            if complexity not in [1, 2, 3]:
                print("Invalid choice. Please select 1, 2, or 3.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        avoid_ambiguous = input("Avoid ambiguous characters (e.g., l, I, 1, O, 0)? (yes/no): ").strip().lower() == 'yes'
        
        # Generate and display the password
        password = generate_password(length, complexity, avoid_ambiguous)
        strength = assess_strength(password)
        print(f"\nGenerated Password: {password}")
        print(f"Password Strength: {strength}")
        
        # Copy to clipboard
        pyperclip.copy(password)
        print("(Password copied to clipboard!)")
        
        # Save to history
        history.append(password)
        if len(history) > 5:  # Limit history to last 5 passwords
            history.pop(0)
        
        # Display password history
        print("\nPassword History:")
        for i, pw in enumerate(history, 1):
            print(f"{i}. {pw}")
        
        # Ask if the user wants to generate another password
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Enhanced Password Generator! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    password_generator()
