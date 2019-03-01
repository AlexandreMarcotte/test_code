from pyqtgraph.Qt import QtGui
import pyqtgraph.opengl as gl
import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph as pg



class Basic3DMoving:
    def __init__(self, w):
        # Create the view
        self.w = w
        self.w.opts['distance'] = 400
        self.w.show()

        # Create the signal 3D
        self.y = np.linspace(0, 100, 100)
        self.x = np.linspace(0, 10, 10)
        temp_z = np.random.rand(len(self.x),len(self.y)) * 8

        cmap = self.create_cmap(temp_z)
        self.surf = gl.GLSurfacePlotItem(
                x=self.x, y=self.y, z=temp_z, colors=cmap)
        w.addItem(self.surf)

    def create_cmap(self, z):
        cmap = plt.get_cmap('jet')
        min_z = np.min(z)
        max_z = np.max(z)
        cmap = cmap((z - min_z)/(max_z - min_z))
        return cmap

    def update(self):
        temp_z = np.random.rand(len(self.x),len(self.y)) * 8
        cmap = self.create_cmap(temp_z)
        print(cmap)
        self.surf.setData(
                x=self.x, y=self.y, z=temp_z, colors=cmap)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    w = gl.GLViewWidget()

    basic_3d_moving = Basic3DMoving(w)
    timer = pg.QtCore.QTimer()
    timer.timeout.connect(basic_3d_moving.update)
    timer.start(5000)

    QtGui.QApplication.instance().exec_()
