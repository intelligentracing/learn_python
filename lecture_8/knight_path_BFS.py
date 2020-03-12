## This is course material for Introduction to Python Scientific Programming
## Class 8 Example code: knight_path_BFS.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

def BFS(board_size, start, goal, legit_moves):
    ''' BFS search a viable path from start position to goal position on the board_size
    Parameters:
    Input:  board_size  - The dimension of the board
            start       - start position of the piece
            goal        - final destination
            legit_moves - describe how the piece can move on the board
    
    Output: result_path - return a BFS path that reaches the goal, otherwise []
    '''

# Assign chess board size. Here half a standard board is used
board_size = (4,8)

# Assign constant tuples for allowed knight's eight moves
knight_moves = ((1,2), (1,-2), (-1,2),(-1,-2), (2,1), (2,-1), (-2,1), (-2,-1))

# Assign knight's initial position
knight_start = (0,0)

# Create a display of the board game problem
print('Game has started, here is the board with the initial position at 0')
board_display = [['*' for i in range(board_size[1])] for j in range(board_size[0])]
board_display[knight_start[0]][knight_start[1]] = '0'
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)

# Acquire user input about the goal position
user_input = input('Please input goal position (x, y): ')
knight_goal = eval(user_input)

print('Moving Knight from {0} to {1}:'.format(knight_start, knight_goal))
board_display[knight_goal[0]][knight_goal[1]]  = '1'
for i in range(board_size[0]):
    display_string = ''.join(board_display[i])
    print(display_string)

knight_path = BFS(board_size, knight_start, knight_goal, knight_moves)