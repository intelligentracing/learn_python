## This is course material for Introduction to Python Scientific Programming
## Class 14 Example code: extract_ETF.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import os

source_filename = 'nasdaqlisted.txt'
result_filename = 'nasdaqetfs.txt'

try:
    path = os.path.dirname(os.path.abspath(__file__))

    source_handle = open(path+'/'+source_filename,'r')
    result_handle = open(path+'/'+result_filename,'w')

    for line in source_handle:
        if 'ETF' in line:
            result_handle.write(line)
except IOError:
    print('IO Error! Please check valid file names and paths')
    exit
finally:
    source_handle.close()
    result_handle.close()
