## This is course material for Introduction to Python Scientific Programming
## Class 17 Example code: estimate_ellipse.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor
from matplotlib.patches import Ellipse
import math

# Initialize the figure and axes
fig = plt.figure()
ax = plt.axes()
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

# Initialize the cursor input
cursor = Cursor(ax, horizOn = True, vertOn = True, color = 'green', linewidth=2.0)

# Initialize the A and b matrices
A = np.zeros((2,2))
b = np.ones(2)
ob_count = 0
theta = np.arange(0, np.pi*2, 0.1)

def onclick(event):
    global ob_count, A, b, theta

    if ob_count==2:
        quit()

    [x, y] = [event.xdata, event.ydata]
    plt.plot(x, y, 'ro')

    # Update A and b
    if x>-10 and x<10 and y>-10 and y<10:
        A[ob_count,0] = x*x; A[ob_count,1] = y*y
        ob_count +=1
    
    if ob_count==2:
        Ainv = np.linalg.inv(A)
        aa = Ainv.dot(b)

        # Plot the ellipse
        if aa[0]<=0 or aa[1]<=0: # a^2, b^2 must be positive
            return
        a = math.sqrt(1/aa[0]); b = math.sqrt(1/aa[1])
        x = a*np.cos(theta); y= b*np.sin(theta)
        plt.plot(x,y,'k-', linewidth = 3)


fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()