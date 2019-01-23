# 'calculate' function is an inside-class thread and main thread use calculated self.y array
import numpy as np
import pyqtgraph as pg
import my_threading
# from Queue import Queue
import time
import random


class FuncThread(my_threading.Thread):
    def __init__(self, t, *a):
        self._t = t
        self._a = a
        my_threading.Thread.__init__(self)

    def run(self):
        self._t(*self._a)


class MyApp(object):
    def __init__(self, x, y):
        self.qapp = pg.mkQApp()
        self.win = pg.GraphicsWindow()
        plot1 = self.win.addPlot()
        curve = plot1.plot()

        self.i = 0
        self.n_steps = 100
        self.x = x
        self.y = y

        calculating_thread = FuncThread(self.calculate)
        calculating_thread.start()

        while self.win.isVisible():
            curve.setData(self.x, self.y)
            self.qapp.processEvents()

    def calculate(self):
        while self.win.isVisible():
            time.sleep(0.01)
            self.i += 1
            if self.i == self.n_steps:
                self.i = 0

            self.y[self.i] = 200


class PlayWithData(my_threading.Thread):
    def __init__(self, x, y):
        super(PlayWithData, self).__init__()
        self.x = x
        self.y = y

    def run(self):
        while 1:
            time.sleep(0.0001)
            self.y[random.randint(0, 100-1)] = random.randint(0, 400)


if __name__ == '__main__':
    n_steps = 100
    x = np.linspace(0, n_steps, n_steps)
    y = np.ones(n_steps)

    play = PlayWithData(x, y)
    play.start()

    m = MyApp(x, y)




