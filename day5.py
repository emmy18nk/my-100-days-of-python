import random

choices = ["rock", "paper", "scissors"]

while True:
    player_choice = input(
        "Choose rock, paper, scissors or Q to quit? "
    ).lower()

    if player_choice == "q":
        print("Thanks for playing!")
        break

    computer_choice = random.choice(choices)

    print(f"Your choice is {player_choice}")
    print(f"Computer choice is {computer_choice}")

    if player_choice == "rock" and computer_choice == "scissors":
        print("You win!")

    elif player_choice == "scissors" and computer_choice == "rock":
        print("You lose!")

    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")

    elif player_choice == "rock" and computer_choice == "paper":
        print("You lose!")

    elif player_choice == "paper" and computer_choice == "scissors":
        print("You lose!")

    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")

    elif player_choice == computer_choice:
        print("It's a draw! Pick again.")

    else:
        print("Invalid selection, pick again.")