## This is course material for Introduction to Python Scientific Programming
## Class 17 Example code: widget_lasso_cursor.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
from matplotlib.widgets import LassoSelector, Cursor

fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_xlim([-10, 0])
ax1.set_ylim([-10, 10])

def onSelect(x):
	print(x)

lineprops = {'color': 'red', 'linewidth': 3, 'alpha': 0.5}
lasso = LassoSelector(ax=ax1, onselect=onSelect, lineprops=lineprops)

ax2 = fig.add_subplot(1,2,2)
ax2.set_xlim([0, 10])
ax2.set_ylim([-10, 10])

cursor = Cursor(ax2,
				horizOn=True, # Controls the visibility of the horizontal line
				vertOn=True, # Controls the visibility of the vertical line
				color='green',
				linewidth=2.0
				)

def onclick(event):
	
    [x1, y1] = [event.xdata, event.ydata]
    if x1>=0:
        print(x1, y1)
        plt.plot(x1,y1, 'ro')
    
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()