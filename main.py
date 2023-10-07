import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

if __name__ == "__main__":
    print("Rock, Paper, Scissors Game")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
