# # -*- coding: utf-8 -*-
# # import to display FFT
# import scipy.fftpack
#
# # PLOTING the EEG data
# # Graph the data
# from pyqtgraph.Qt import QtGui
# import numpy as np
# import pyqtgraph as pg
# from pyqtgraph.ptime import time
# import multiprocessing
# from collections import deque
# import time
# from random import random
# import my_threading
#
#
# class UpdateMultipleChPlot(object):
#     def __init__(self, plot, curve, data):
#         self.plot = plot
#         self.curve = curve
#         self.data = data
#
#     def update_eeg(self, sample, timestamp, ch):
#         self.plot[ch].setLabel('right', '{mean_ampl:.2f} muVrms'.format(
#                                           mean_ampl=np.mean(self.data[ch])))    # TODO: verifier l'unité
#         self.data[ch].append(sample)
#         self.curve[ch].setData(self.data[ch])
#
#
# class FrequencyCounter(object):
#     def __init__(self, loop_name):
#         self.initial_time = time.time()
#         self.last_time_elapsed = 0
#         self.loop_name = loop_name
#
#     def print_freq(self, n_val_created):
#         """ Plot the frequency of a loop once every second"""
#         time_elapsed = int(time.time() - self.initial_time)
#         if time_elapsed > self.last_time_elapsed:
#             self.last_time_elapsed = time_elapsed
#             print('--------',
#                   'time_elapsed:', time_elapsed,
#                   'n_val_created:', n_val_created,
#                   'FREQUENCY: ', n_val_created / time_elapsed,
#                   'of {l_n}'.format(l_n=self.loop_name))
#
#
# class MultiChannelsPyQtGraph(object):
#     def __init__(self, data_queue, time_queue, N_DATA=200, N_SIGNALS=8):
#         """
#
#         """
#         self.data_queue = data_queue
#         self.time_queue = time_queue
#         # Initialize window value
#         self.win = pg.GraphicsWindow()
#         # Create 8 scrolling plot on the left of the window
#         # To display all the channels
#         self.N_DATA = N_DATA
#         self.N_SIGNALS = N_SIGNALS
#         self.p = [[]] * self.N_SIGNALS
#         self.data = [None] * self.N_SIGNALS
#         self.curve = [None] * self.N_SIGNALS
#         self.update_func = []
#         self.NUM_ITT = 0
#         self.DISPLAY_RATE = 1
#         # Create the EEG channels
#         self.create_eeg_channels()
#         # FFT plot
#         self.p_freq = None
#         self.curve_freq = None
#         self.create_fft_channel()
#         self.last_queue_val = []                                                # TODO: ALEXM: probably better to use a Queue or a numpy array
#         self.FFT_calculated = False
#         #
#         self.frequency_counter = FrequencyCounter('EEG_frequency')
#
#     def create_eeg_channels(self):
#         self.win.setWindowTitle('Visualisation of OPENBCI signals widget')
#         self.win.useOpenGL()
#         # Create all the  8 plots, there title and axis values
#         for ch in range(self.N_SIGNALS):
#             self.p[ch] = self.win.addPlot(row=ch, col=0)
#             # Create plot labels
#             self.set_plot_labels(ch)
#
#             self.data[ch] = deque(np.zeros(self.N_DATA), maxlen=self.N_DATA)
#             self.curve[ch] = self.p[ch].plot(self.data[ch])
#             # Create one update object for every channel
#             update_eeg = UpdateMultipleChPlot(self.p, self.curve, self.data)
#
#             self.update_func.append(update_eeg)
#
#     def set_plot_labels(self, ch):
#         # Add axis labels
#         self.p[ch].setLabel('left', 'ch {i}'.format(i=ch))
#         if ch == 0:
#             self.p[ch].setTitle("""Electrical amplitude of the signal
#                                    for the 8 channels of the OPENBCI""")
#         if ch == self.N_SIGNALS - 1:
#             self.p[ch].setLabel('bottom', 'Time', 's')
#         self.p[ch].showGrid(x=True, y=True, alpha=0.3)
#
#     def update_eeg_plotting(self):
#         # Get one N_SIGNALS channels list
#         data_tmp = self.data_queue.get()
#         time_tmp = self.time_queue.get()
#         # Show signal only once every DISPLAY_RATE iterations
#         if self.NUM_ITT % self.DISPLAY_RATE == 0:  # Plot every 'NUM_ITT' samples
#             # self.NUM_ITT = 0
#             self.frequency_counter.print_freq(self.NUM_ITT)
#             # -Store eeg value of a single EEG channel to calculate its FFT-
#             self.last_queue_val.append(data_tmp[0])
#             # --Remove the value once the FFT was calculated (once every cycle)--
#             if self.FFT_calculated:
#                 self.last_queue_val = []
#                 self.FFT_calculated = False
#             # Update every single channels
#             for ch in range(self.N_SIGNALS):
#                 self.update_func[ch].update_eeg(data_tmp[ch], time_tmp, ch)
#         self.NUM_ITT += 1
#
#     def create_fft_channel(self):
#         """Create a frequency plot on the side"""
#         self.p_freq = self.win.addPlot(rowspan=8, row=0, col=1)
#         self.p_freq.setLabel('bottom', 'Frequency', 'hz')
#         self.p_freq.setTitle('FFT for all channels')
#         self.p_freq.showGrid(x=True, y=True, alpha=0.5)
#
#     def update_fft_plotting(self):
#         # Calculate the FFT value once every 100 values received
#         if len(self.last_queue_val) == 100:
#             self.FFT_calculated = True
#             data_freq = deque(np.zeros(self.N_DATA), maxlen=self.N_DATA)
#             self.curve_freq = self.p_freq.plot(data_freq)
#             yf = scipy.fftpack.fft(self.last_queue_val)
#             # Set x axis
#             xf = np.linspace(0.0, 250.0, len(data_freq) // 2)
#             self.p_freq.setRange(xRange=xf)
#             self.curve_freq.setData(2.0 / len(data_freq)
#                                   * np.abs(yf[:len(data_freq) // 2]))
#
#     def update_all_plots(self):
#         # self.update_fft_plotting()
#         self.update_eeg_plotting()
#
#     def exec_plot(self):
#         timer = pg.QtCore.QTimer()
#         timer.timeout.connect(self.update_all_plots)
#         timer.start(0)
#         QtGui.QApplication.instance().exec_()
#
#
# class CreateFakeData(my_threading.Thread):
#     def __init__(self, data_queue):
#         super(CreateFakeData, self).__init__()
#         self.data_queue = data_queue
#         # self.time_queue = time_queue
#         self.n_val_created = 0
#         self.freq_counter = FrequencyCounter(loop_name='creatingFakeData')
#
#     def run(self):
#         """Create random data and a time stamp for each of them"""
#         while 1:
#             self.n_val_created += 1
#             # print('N_VAL_CREATED: ', self.n_val_created)
#             # Print frequency of the run function once every second
#             self.freq_counter.print_freq(self.n_val_created)
#             # print('TIME: _____', )
#             data_queue.append([self.n_val_created for _ in range(8)])
#             # data_queue.put([self.n_val_created for _ in range(8)])
#             time_queue.put(time.time())
#             # time.sleep(0.004)
#
#
# if __name__ == '__main__':
#     # time_queue = multiprocessing.Queue(maxsize=5000)
#     # data_queue = multiprocessing.Queue(maxsize=5000)
#     DEQUE_LEN = 200
#     data_queue = deque(maxlen=DEQUE_LEN)
#     for _ in range(DEQUE_LEN):
#         data_queue.append(np.zeros(8))
#
#     # Create fake data for test case
#     create_fake_data = CreateFakeData(data_queue)
#     create_fake_data.start()
#     # Start the multigraphes
#     multich_plot = MultiChannelsPyQtGraph(data_queue, time_queue)
#     multich_plot.update_eeg_plotting()
#     multich_plot.exec_plot()
#
#
#
#
#
#
#
#
#
#
#
#
#
