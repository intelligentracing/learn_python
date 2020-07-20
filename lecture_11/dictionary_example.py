## This is course material for Introduction to Python Scientific Programming
## Class 11 Example code: dictionary_example.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

English_to_Chinese = dict()

# building a short translation dictionary
English_to_Chinese['one'] = '一'
English_to_Chinese['two'] = '二'
English_to_Chinese['three'] = '三'

print(English_to_Chinese['two'])

print('three' in English_to_Chinese)

# Build a character histogram

histogram = dict()
text = 'We can know only that we know nothing. \
    And that is the highest degree of human wisdom.' # From War and Peace

for c in text:
    if c.isalpha():
        c = c.lower()
        if c in histogram:
            histogram[c] += 1
        else:
            histogram[c] = 1

for key in histogram:
    print(key, end = ' ')
print()
for key in histogram:
    print(histogram[key], end = ' ')
