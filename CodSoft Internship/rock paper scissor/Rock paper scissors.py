# Game options
options = ["rock", "paper", "scissors"]

def get_computer_choice():
    return get_computer_choice.choice(['rock','paper','scissors'])

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in options:
        choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Run the game
play_game();
