# from PyQt5 import QtGui, QtCore
# import pyqtgraph as pg
# import numpy as np
# import sys
#
#
# class ScrollingPlot(object):
#     def __init__(self, plot_obj):
#         self.data1 = np.random.normal(size=300)
#         self.curve1 = plot_obj.plot(self.data1)
#
#     def update(self):
#         self.data1[:-1] = self.data1[1:]
#         self.data1[-1] = np.random.normal()
#         self.curve1.setData(self.data1)
#
# def main():
#     app = pg.mkQApp()
#     layout = pg.LayoutWidget()
#     # b1 = QtGui.QPushButton('plot local')
#
#     # layout.addWidget(b1)
#
#
#     # my_plots = []
#
#     # for i in range(8):
#     #     plot = pg.PlotWidget()
#     #     # if i == 7:
#     #     #     col = 1
#     #     #     rowspan = 4
#     #     #     row = 4
#     #     # else:
#     #     #     col = 0
#     #     #     rowspan = 1
#     #     #     row = i+1
#     #     layout.addWidget(plot, row=i+1, col=0, rowspan=1)
#     #
#     #     my_plots.append(ScrollingPlot(plot))
#     #     timer.timeout.connect(my_plots[i].update)à
#     timer = QtCore.QTimer()
#     plot = pg.PlotWidget()
#     layout.addWidget(plot, row=1, col=0)
#     my_plot = ScrollingPlot(plot)
#     timer.timeout.connect(my_plot.update)
#
#     layout.show()
#
#     timer.start(0)
#     sys.exit(app.exec_())
#
# if __name__ == '__main__':
#     main()
#
#



