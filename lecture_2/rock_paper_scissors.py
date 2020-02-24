import random

# Ask user to input 1 or 2 or 3
print("Please input [1] Rock, [2] Paper, or [3] Scissors")
user_input = int(input())

if user_input !=1 and user_input !=2 and user_input !=3:
    print("Input not supported")
else:
    computer_input = random.randint(1,3)
    print("Computer input is ", computer_input)
    if computer_input == user_input:
        print("Draw!")
    elif computer_input - user_input == 1 or computer_input-user_input == -2:
        print("You Lost!")
    else:
        print("You Win!")