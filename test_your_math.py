# import two Python modules
import random   # includes functions for generating random numbers
import math     # includes additional math functions

# Define constants
OPERATOR_ROUND = 1
OPERATOR_INT = 2
OPERATOR_FLOOR = 3
OPERATOR_CEIL = 4

score = 0
print("*** Test Your int/float Math Skills ***")
print("*** Let's Begin: Your Score is 0")
while True:
    random_operator = random.randint(1,4)
    random_A = random.randint(-10,10)
    random_B = random.randint(-10,10)
    if random_operator == OPERATOR_ROUND:
        result = round(random_A/random_B)
        operator_string = "round"
    elif random_operator == OPERATOR_INT:
        result = int(random_A/random_B)
        operator_string = "int"
    elif random_operator == OPERATOR_FLOOR:
        result = math.floor(random_A/random_B)
        operator_string = "floor"
    else:
        result = math.ceil(random_A/random_B)
        operator_string = "ceil"

    question_string = "Question: " + str(operator_string) + "(" + str(random_A) + "/" + str(random_B) + ") = ? "
    user_result = input(question_string)
    user_result = int(user_result)
    if  user_result == result:
        score = score + 1
    else:
        score = score - 1

    print("Your current score: ", score)
