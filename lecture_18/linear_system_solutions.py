## This is course material for Introduction to Python Scientific Programming
## Class 18 Example code: linear_system_solutions.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import numpy as np
from matplotlib.widgets import Slider
import matplotlib.pyplot as plt

# Initialize the linear system
x = np.arange(0,50,1)
A = np.array([[1,1], [4,2]])
bb = np.array([[35],[110]])
fig, ax = plt.subplots()
plt.subplots_adjust(bottom = 0.25)

def draw_systems():
    global legend_handle

    ax.clear()
    y1 = (bb[0,0] - A[0,0]*x)/A[0,1]
    y2 = (bb[1,0] - A[1,0]*x)/A[1,1]

    line1, = ax.plot(x, y1, 'r', linewidth = 3)
    line1.set_label(str(A[0,0])+'x + '+str(A[0,1])+'y = ' + str(bb[0,0]))
    line2, = ax.plot(x, y2, 'b', linewidth = 3)
    line2.set_label(str(A[1,0])+'x + '+str(A[1,1])+'y = ' + str(bb[1,0]))

    # Update intersection
    # First test uniqueness
    if A[0,0]/A[0,1] != A[1,0] / A[1,1]:
        xx = np.linalg.inv(A) @ bb        # Another notation for dot product
        intersection, = ax.plot(xx[0,0], xx[1,0], 'kD', markersize = 8)
        intersection.set_label('('+str(xx[0,0])+', ' + str(xx[1,0])+')')

    legend_handle=ax.legend()
    fig.canvas.draw_idle()

# Create initial plot
draw_systems()

# Create two sliders
axcolor = 'lightgoldenrodyellow'
axA00 = plt.axes([0.25, 0.15, 0.5, 0.03], facecolor = axcolor)
axb00 = plt.axes([0.25, 0.10, 0.5, 0.03], facecolor = axcolor)
A00_slider = Slider(axA00, 'A[0,0]', -3, 5, valinit = 1, valstep = 1)
b00_slider = Slider(axb00, 'b[0,0]', 15, 55, valinit = 35, valstep = 5)

def update(val):
    A[0,0] = A00_slider.val
    bb[0,0] = b00_slider.val
    draw_systems()
A00_slider.on_changed(update)
b00_slider.on_changed(update)

plt.show()