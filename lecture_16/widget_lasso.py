## This is course material for Introduction to Python Scientific Programming
## Class 16 Example code: widget_lasso_cursor.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
from matplotlib.widgets import LassoSelector, Cursor

fig, ax = plt.subplots()

def onSelect(x):
	print(x)

lineprops = {'color': 'red', 'linewidth': 3, 'alpha': 0.5}
lsso = LassoSelector(ax=ax, onselect=onSelect, lineprops=lineprops)

plt.show()

fig, ax = plt.subplots()

cursor = Cursor(ax,
				horizOn=True, # Controls the visibility of the horizontal line
				vertOn=True, # Controls the visibility of the vertical line
				color='green',
				linewidth=2.0
				)

def onclick(event):
	x1, y1 = event.xdata, event.ydata
	print(x1, y1); plt.plot(x1,y1, 'ro')
    
fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()