## This is course material for Introduction to Python Scientific Programming
## Class 2 Example code: rock_paper_scissors.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import random

# Ask user to input R or P or S
user_input = input("Please input [R] Rock, [P] Paper, or [S] Scissors: ")   # input is a string type

if user_input !='R' and user_input !='P' and user_input !='S': # Doing exception test
    print("Input not supported")
else:
    computer_input = random.choice(['R', 'P', 'S'])
    print("Computer input is ", computer_input)
    if computer_input == user_input:
        print("Draw!")
    elif (computer_input=='R' and user_input == 'S') or \
        (computer_input=='S' and user_input == 'P') or \
        (computer_input=='P' and user_input == 'R'):
        print("You Lose!")
    else:
        print("You Win!")