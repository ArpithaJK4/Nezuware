import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play one round of the game
def play_round():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    # Validate input
    while player_choice not in choices:
        print("Invalid input! Please enter rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    print(f"Computer chose: {computer_choice}")
    result = determine_winner(player_choice, computer_choice)
    print(result)

    return result

# Function to track the score and manage multiple rounds
def rock_paper_scissors_game():
    player_score = 0
    computer_score = 0
    rounds = 0

    print("Welcome to Rock, Paper, Scissors game!")
    print("Enter 'quit' to stop playing.\n")

    while True:
        rounds += 1
        print(f"--- Round {rounds} ---")
        result = play_round()

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        # Option to quit
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again == 'no':
            break

    # Display final score
    print("\nGame over!")
    print(f"Final Score:\nYou: {player_score} | Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations, you won the game!")
    elif player_score < computer_score:
        print("Computer won the game! Better luck next time.")
    else:
        print("The game ended in a tie!")

# Run the game
rock_paper_scissors_game()
