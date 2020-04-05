## This is course material for Introduction to Python Scientific Programming
## Class 16 Example code: matplotlib_clock.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime
import matplotlib.pyplot as plt

# First retrieve the time
now_time = datetime.now()
time = now_time.split(' ')
hour, minute, second = time.split(":")

# draw an image background

