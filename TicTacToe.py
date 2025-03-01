import random

# Instructions
instructions = """
This will be our tic tac toe board

 1 | 2 | 3 
---|---|---
 4 | 5 | 6 
---|---|---
 7 | 8 | 9 

*instructions:
1. Insert the spot number(1-9) to put your sign,
2. You must fill all 9 spots to get result,
3. Player 1 will go first.
"""

# Initialize the board
sign_dict = [' ' for _ in range(9)]

def print_board(sign_dict):
    board = f"""
     {sign_dict[0]} | {sign_dict[1]} | {sign_dict[2]}
    ---|---|---
     {sign_dict[3]} | {sign_dict[4]} | {sign_dict[5]}
    ---|---|---
     {sign_dict[6]} | {sign_dict[7]} | {sign_dict[8]}
    """
    print(board)

def take_input():
    while True:
        try:
            x = int(input("Enter your move (1-9): ")) -1
            if 0 <= x < 9 and sign_dict[x] == ' ':
                return x
            print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

def is_moves_left(sign_dict):
    return ' ' in sign_dict

def evaluate(sign_dict, sign):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(sign_dict[i] == sign for i in condition):
            return True
    return False

def minimax(board, depth, is_max):
    if evaluate(board, 'X'):
        return 10 - depth
    if evaluate(board, 'O'):
        return depth - 10
    if not is_moves_left(board):
        return 0

    if is_max:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                best = max(best, minimax(board, depth + 1, not is_max))
                board[i] = ' '
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                best = min(best, minimax(board, depth + 1, not is_max))
                board[i] = ' '
        return best

def find_best_move(board):
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

def main():
    print("Welcome to Tic-Tac-Toe game!")
    player_name = input("Enter player name: ")
    player_name=player_name.capitalize()
    print(instructions)
    print(f"Thank you for joining the game {player_name}")
    print("Your sign is - O")
    print("System's sign is - X")
    input("Enter enter key to start the game")
    print_board(sign_dict)

    for i in range(9):
        if i % 2 == 0:
            if i == 0:
                best_move = random.choice([index for index, val in enumerate(sign_dict) if val == ' '])
            else:
                best_move = find_best_move(sign_dict)
            sign_dict[best_move] = 'X'
            print("System's move:")
        else:
            index = take_input()
            sign_dict[index] = 'O'
        
        print_board(sign_dict)
        
        if evaluate(sign_dict, 'X'):
            print("You Lost Game,Play again!")
            break
        elif evaluate(sign_dict, 'O'):
            print(f"Congratulations {player_name}. You won the game!")
            break
    else:
        print("This is a tie! Nobody won.")

main()