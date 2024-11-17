import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

# Function to display feedback for each round
def display_feedback(winner):
    if winner == "tie":
        return random.choice([
            "It's a draw! Great minds think alike!",
            "Tie! Both of you are equally matched!"
        ])
    elif winner == "user":
        return random.choice([
            "You win! Well played!",
            "Victory is yours! Keep it up!"
        ])
    elif winner == "computer":
        return random.choice([
            "Computer wins! Better luck next time!",
            "Ouch! The computer got the better of you."
        ])

# Main function to play the game
def rock_paper_scissors_game():
    print("Welcome to the Rock-Paper-Scissors Game!")
    print("Instructions:")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to end the game.\n")

    user_score = 0
    computer_score = 0
    game_history = []

    while True:
        user_choice = input("Your choice (rock/paper/scissors): ").lower()

        if user_choice not in ['rock', 'paper', 'scissors', 'exit']:
            print("Invalid choice. Please try again.")
            continue

        if user_choice == 'exit':
            print("\nGame Over!")
            print(f"Final Scores: You: {user_score}, Computer: {computer_score}")
            print("\nGame History:")
            for round_num, (user, computer, result) in enumerate(game_history, 1):
                print(f"Round {round_num}: You chose {user}, Computer chose {computer} -> {result}")
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        feedback = display_feedback(winner)
        print(f"\nYou chose: {user_choice}, Computer chose: {computer_choice}")
        print(feedback)
        print(f"Scores -> You: {user_score}, Computer: {computer_score}\n")

        # Save the round result to game history
        result = "You won!" if winner == "user" else "Computer won!" if winner == "computer" else "Tie"
        game_history.append((user_choice, computer_choice, result))

# Run the game
if __name__ == "__main__":
    rock_paper_scissors_game()
