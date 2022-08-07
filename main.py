from random import randrange

# Prints the board
def display_board():
    visual = (f"+-------+-------+-------+\n"
            f"|       |       |       |\n"
            f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |\n"
            f"|       |       |       |\n"
            f"+-------+-------+-------+\n"
            f"|       |       |       |\n"
            f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |\n"
            f"|       |       |       |\n"
            f"+-------+-------+-------+\n"
            f"|       |       |       |\n"
            f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |\n"
            f"|       |       |       |\n"
            f"+-------+-------+-------+")
    
    print(visual)

# Receives the move from the user and checks if it is valid
def enter_move():
    input_check = True
    
    # Creates an infinite loop that will check if the move is valid
    while input_check:
        user_move = int(input('Enter your move: '))
        # Checks if the move is in 1-10 and if it's a 5 (the first move from the computer)
        if user_move not in range(1,10) or user_move == 5:
            print('Invalid input, try again.')
            display_board()
            continue
        else:
            # Transforms from a number to a coordinate
            if user_move == 1: user_move = (0,0)
            if user_move == 2: user_move = (0,1)
            if user_move == 3: user_move = (0,2)
            if user_move == 4: user_move = (1,0)
            if user_move == 6: user_move = (1,2)
            if user_move == 7: user_move = (2,0)
            if user_move == 8: user_move = (2,1)
            if user_move == 9: user_move = (2,2)
            
            # Checks if the field is free
            if user_move not in free_fields:
                print('Invalid input, try again.')
                display_board()
                continue
            else:
                board[user_move[0]][user_move[1]] = 'O'
                display_board()
                input_check = False

# Makes a list of free fields
def make_list_of_free_fields():
    del free_fields[:]
    for row in range(3):
        for col in range(3):
            if not board[row][col] == 'X' and not board[row][col] == 'O':
                free_fields.append((row,col))

# Checks if anyone has won the game
def victory_for():
    end = False
    winner = None
    count = 0
    
    # Horizontally
    if board[0][0] == board[0][1] == board[0][2]: 
        if board[0][0] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    if board[1][0] == board[1][1] == board[1][2]: 
        if board[1][0] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    if board[2][0] == board[2][1] == board[2][2]: 
        if board[2][0] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    # Vertically
    if board[0][0] == board[1][0] == board[2][0]: 
        if board[0][0] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    if board[0][1] == board[1][1] == board[2][1]: 
        if board[0][1] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    if board[0][2] == board[1][2] == board[2][2]: 
        if board[0][2] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    # Diagonally
    if board[0][0] == board[1][1] == board[2][2]: 
        if board[0][0] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    if board[2][0] == board[1][1] == board[0][2]: 
        if board[2][0] == 'X': winner = 'X'
        else: winner = 'O'
        end = True
    
    # Tie
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X' or board[row][col] == 'O':
                count += 1
    if count == 9:
        display_board()
        print('Tie')
        end = True
    else:
        count = 0
    
    # Prints if the user won or lose
    if winner == 'O':
        print('You won!')
    elif winner == 'X':
        display_board()
        print('You lose!')
    
    return end

# Draws the computer's move
def draw_move():
    input_check = True
    
    while input_check:
        pc_move = (randrange(3),randrange(3))
        if pc_move in free_fields:
            board[pc_move[0]][pc_move[1]] = 'X'
            input_check = False

# Creates the initial board
board = [
    [1,2,3],
    [4,'X',6],
    [7,8,9]
]

playing = True
free_fields = []

# Creates an infinite loop where the game is loaded
while playing:
    display_board()
    make_list_of_free_fields()
    enter_move()
    if victory_for(): playing = False
    else:
        make_list_of_free_fields()
        draw_move()
        if victory_for(): playing = False