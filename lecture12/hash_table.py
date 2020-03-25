## This is course material for Introduction to Python Scientific Programming
## Class 12 Example code: hash_table.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

def division_hashing(text):
    global hash_prime_number
    hash_prime_number = 101

    sum = 0
    for c in text:
        sum = sum + (ord(c)*256) % hash_prime_number  # Change a character to its ASCII value
    
    return sum % hash_prime_number

def hash_table_insert(table, entry):

    if type(table)!=dict:
        raise TypeError('Argument 1 must be a dict type')

    entry_hash = division_hashing(entry)
    if entry_hash in table:
        table[entry_hash].append(entry)
    else: 
        table[entry_hash] = [entry]

quotes = ['We can know only that we know nothing. And that is the highest degree of human wisdom.',\
        'Nothing is so necessary for a young man as the company of intelligent women.',\
        'The strongest of all warriors are these two — Time and Patience.',\
        'There is no greatness where there is not simplicity, goodness, and truth.'
        ]
string = quotes[0]
hash_table = dict()
for index in range(len(string) - 3 + 1):
        substring = string[index:index+3]
        hash_table_insert(hash_table, substring)

for key in hash_table:
    print(key, hash_table[key])