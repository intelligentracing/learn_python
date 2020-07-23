## This is course material for Introduction to Python Scientific Programming
## Class 12 Example code: set_search_speed.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import os
import random
import time

Set10 = set()
Set1000 = set()
SetTotal = set()
file_name = "nasdaqlisted.txt"

# Put IO functions in try -- finally 
print('Reading IO file ... ', end = ' ')
try:
    # Get the script path

    path = os.path.dirname(os.path.abspath(__file__))

    # Open the file for read
    f_handle = open(path+'/'+file_name,"r")
    f_handle.readline()

    # Create three sets of different lengths
    count = 0
    for line in f_handle:
        count += 1
        ticker, info = line.split('|',1)
        if count<=10:
            Set10.add(ticker)
        if count<=1000:
            Set1000.add(ticker)
        SetTotal.add(ticker)

except IOError:
    print('Cannot open the file ' + file_name)
    exit
finally:
    f_handle.close()

print('done')
            
# Create 1M queries to time the performance of three sets
print('Generating 1M random tickers ... ', end = ' ')
trial_total = 1000000
TICKER_LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
search_list = []
for index in range(trial_total):
    new_random_ticker = ''
    for letter_index in range(random.randint(1,5)):
        new_random_ticker = new_random_ticker + (random.choice(TICKER_LETTER))
    
    search_list.append(new_random_ticker)
print('done')

# Test speed for query Set10
begin_time = time.time()
for index in range(trial_total):
    query_result = search_list[index] in Set10
elapsed_time = time.time() - begin_time
print("Searching a size-{0} set 1M times takes: {1}s".format(len(Set10), elapsed_time))

# Test speed for query Set10
begin_time = time.time()
for index in range(trial_total):
    query_result = search_list[index] in Set1000
elapsed_time = time.time() - begin_time
print("Searching a size-{0} set 1M times takes: {1}s".format(len(Set1000), elapsed_time))

# Test speed for query Set10
begin_time = time.time()
for index in range(trial_total):
    query_result = search_list[index] in SetTotal
elapsed_time = time.time() - begin_time
print("Searching a size-{0} set 1M times takes: {1}s".format(len(SetTotal), elapsed_time))
