## This is course material for Introduction to Python Scientific Programming
## Class 12 Example code: hash_search.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

quotes = ['We can know only that we know nothing. And that is the highest degree of human wisdom.',\
        'Nothing is so necessary for a young man as the company of intelligent women.',\
        'The strongest of all warriors are these two — Time and Patience.',\
        'There is no greatness where there is not simplicity, goodness, and truth.'
        ]

def division_hashing(text):
    global hash_prime_number
    hash_prime_number = 101

    sum = 0
    for c in text:
        sum = sum*256 + ord(c)  # Change a character to its ASCII value
    
    return sum % hash_prime_number

print(division_hashing(quotes[0]), division_hashing(quotes[1]), division_hashing(quotes[2]), division_hashing(quotes[3]))