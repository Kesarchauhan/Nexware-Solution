import random
import string

# Function to generate a password
def generate_password(length, complexity):
    characters = string.ascii_lowercase
    if complexity >= 2:
        characters += string.ascii_uppercase + string.digits
    if complexity == 3:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/|"
    
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
        
        # Generate and display the password
        password = generate_password(length, complexity)
        strength = assess_strength(password)
        print(f"\nGenerated Password: {password}")
        print(f"Password Strength: {strength}")
        
        # Save to history
        history.append(password)
        if len(history) > 5:  # Limit history to last 5 passwords
            history.pop(0)
            
        print("\nPassword History:")
        for i, pw in enumerate(history, 1):
            print(f"{i}. {pw}")
        
 
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Enhanced Password Generator! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    password_generator()
