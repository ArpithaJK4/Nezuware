
# Function to print the Tic Tac Toe board
def print_board(board):
    print("\n")
    for row in board:
        print("|".join(row))
        print("-" * 5)
    print("\n")

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

# Function to check if the board is full (i.e., a draw)
def is_draw(board):
    return all([spot != ' ' for row in board for spot in row])

# Function to play one round of Tic Tac Toe
def play_round():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        # Get player input and validate it
        try:
            row = int(input(f"Player {current_player}, enter the row (1-3): ")) - 1
            col = int(input(f"Player {current_player}, enter the column (1-3): ")) - 1

            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter numbers between 1 and 3.")
                continue

            if board[row][col] != ' ':
                print("This spot is already taken! Choose another spot.")
                continue

            # Mark the player's move on the board
            board[row][col] = current_player
            print_board(board)

            # Check for a winner or a draw
            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break
            elif is_draw(board):
                print("It's a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'
        
        except ValueError:
            print("Invalid input! Please enter numbers only.")

# Function to manage multiple games
def tic_tac_toe_game():
    while True:
        play_round()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Run the game
tic_tac_toe_game()
