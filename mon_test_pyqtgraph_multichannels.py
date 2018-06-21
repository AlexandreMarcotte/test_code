# -*- coding: utf-8 -*-
#%% # TODO: (ALEX)
"""
1. Remove thie file from the OPENBCI files and add the path to the required
   files so that the interpreter still can reach them

"""

#%%
import matplotlib.pyplot as plt
import numpy as np
import time
import scipy.fftpack

#%% PLOTING the EEG data
# Graph the data
from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
from pyqtgraph.ptime import time
app = QtGui.QApplication([])
# For the EEG feed
from collections import deque
import time
from random import random

class MultiChannelsPyQtGraph(object):
    def __init__(self):
        win = pg.GraphicsWindow()
        win.setWindowTitle('Visualisation of OPENBCI signals widget')
        win.useOpenGL()
        # Create 8 scrolling plot at the left of the screen to display all channels
        N_DATA = 500
        N_SIGNALS = 8
        p = [[]] * N_SIGNALS
        data = [None] * N_SIGNALS
        self.curve = [None] * N_SIGNALS
        update_func = []
        # Create all the  8 plots and there title and axis values
        for i in range(N_SIGNALS):
            p[i] = win.addPlot(row=i, col=0)
            # add axis labels
            p[i].setLabel('left', 'ch {i}'.format(i=i))
            if i == 0:
                p[i].setTitle("""Electrical amplitude of the signal for
                                 the 8 channels of the OPENBCI""")
            if i == 7:
                p[i].setLabel('bottom', 'Time', 's')
            p[i].showGrid(x=True, y=True, alpha=0.3)

            data[i] = deque(np.zeros(N_DATA), maxlen=N_DATA)
            curve[i] = p[i].plot(data[i])
            def update(sample, timestamp, i):
                self.curve
                p[i].setLabel('right',
                              '{mean_ampl:.2f} muVrms'.format(mean_ampl=np.mean(data[i])))      # TODO: verifier l'unité
                data[i].append(sample)
                curve[i].setData(data[i])
            update_func.append(update)

        self.num_itt = 0

    def update(self):
        # Using chunk to avoid laging behind time by having a displaying rate
        # lower than the sampling rate
        DISPLAY_RATE = 1
        # Create random data and a time stamp for each of them
        samples = [random() for _ in range(8)]
        timestamp = time.time()

        if self.num_itt % DISPLAY_RATE == 0: # plot every 5 samples
            self.num_itt = 0
            # Update the 8 signal channels
            for i in range(N_SIGNALS):
                update_func[i](samples[i], timestamp, i)
        self.num_itt += 1

    timer = pg.QtCore.QTimer()
    timer.timeout.connect(update)
    timer.start(0)

# Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    QtGui.QApplication.instance().exec_()







