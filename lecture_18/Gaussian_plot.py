## This is course material for Introduction to Python Scientific Programming
## Class 18 Example code: Gaussian_plot.py
## Author: Allen Y. Yang,  Intelligent Racing Inc.
##
## (c) Copyright 2020. Intelligent Racing Inc. Not permitted for commercial use

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math
from matplotlib.widgets import Slider

# Initialize the figure
fig, ax = plt.subplots()
plt.subplots_adjust(bottom = 0.25)

# Initialize a Gaussian model
mu = 0
sigma = 1
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
l, = plt.plot(x, stats.norm.pdf(x, mu, sigma))

axmu = plt.axes([0.25, 0.1, 0.5, 0.03])
axsigma = plt.axes([0.25, 0.15, 0.5, 0.03])
smu = Slider(axmu, 'Mu', -5, 5, valinit = 0)
ssigma = Slider(axsigma, "Sigma", 0, 5, valinit = 1)

def update(val):
    global mu, sigma

    mu = smu.val
    sigma = ssigma.val
    l.set_ydata(stats.norm.pdf(x, mu, sigma))
    fig.cancas.draw_idle()

smu.on_changed(update)
ssigma.on_changed(update)

plt.show()