import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 'user'
    else:
        return 'computer'

def print_result(winner, user_choice, computer_choice):
    print(f"\nYou chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    if winner == 'tie':
        print("It's a tie!")
    elif winner == 'user':
        print("Congratulations! You win!")
    else:
        print("Sorry, you lose. Better luck next time.")

def play_game():
    user_choice = get_user_choice()
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    winner = determine_winner(user_choice, computer_choice)

    print_result(winner, user_choice, computer_choice)

if __name__ == "__main__":
    play_game()
