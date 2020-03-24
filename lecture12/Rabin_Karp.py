## This is course material for Introduction to Python Scientific Programming
## Class 12 Example code: Rabin_Karp.py
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

def Rabin_Karp(string, pattern):

    if type(string)!=str or type(pattern)!=str:
        raise TypeError('Arguments must be str type')

    result = []
    pattern_len = len(pattern)
    string_len = len(string)
    if pattern_len>string_len:
        return result
    
    pattern_hash = division_hashing(pattern)
    for index in range(string_len - pattern_len + 1):
        substring = string[index:index+pattern_len]
        substring_hash = division_hashing(substring)
        if substring_hash == pattern_hash:
            result.append(index)
    
    return result

quotes = ['We can know only that we know nothing. And that is the highest degree of human wisdom.',\
        'Nothing is so necessary for a young man as the company of intelligent women.',\
        'The strongest of all warriors are these two — Time and Patience.',\
        'There is no greatness where there is not simplicity, goodness, and truth.'
        ]

pattern = 'man'

print(Rabin_Karp(quotes[0], pattern))