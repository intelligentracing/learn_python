## This is course material for Introduction to Python Scientific Programming
## Class 16 Example code: matplotlib_clock.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

from datetime import datetime
import matplotlib.pyplot as plt
import os
import numpy as np

# Initialization, define some constant
path = os.path.dirname(os.path.abspath(__file__))
filename = path + '/airplane.bmp'
second_hand_lengh = 200
second_hand_width = 2
minute_hand_length = 150
minute_hand_width = 4
hour_hand_length = 100
hour_hand_width = 10
center = [256, 256]

# First retrieve the time
now_time = datetime.now()
hour = now_time.hour
minute = now_time.minute
second = now_time.second

# draw an image background
background = plt.imread(filename)
fig, ax = plt.subplots()
plt.imshow(background)

plt.arrow()

plt.show()
