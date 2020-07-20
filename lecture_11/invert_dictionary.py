## This is course material for Introduction to Python Scientific Programming
## Class 11 Example code: invert_dictionary.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

# Build a histogram dictionary
histogram = dict()
text = 'We can know only that we know nothing. And that is the highest degree of human wisdom.' # From War and Peace

for c in text:
    if c.isalpha():
        c = c.lower()
        if c in histogram:
            histogram[c] += 1
        else:
            histogram[c] = 1

def invert_dictionary(input_dictionary):
    '''
    Invert the mapping between keys and values of a dictionary
    Parameters
    Input:  input_dictionary    - a dict type
    Output: result              - dict result
    '''

    if type(input_dictionary)!=dict:
        raise TypeError('Argument must be dict type.')

    result = dict()
    for key in input_dictionary:
        value = input_dictionary[key]
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)
    
    return result

# print out the histogram
for key in histogram:
    print(key, end = ' ')
print()
for key in histogram:
    print(histogram[key], end = ' ')
print()
# Call invert_dictionary 
inverse = invert_dictionary(histogram)
print(inverse)