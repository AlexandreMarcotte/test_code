# https://www.youtube.com/watch?v=a1kxPd8Mdhw
import numpy as np
from pyqtgraph import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import sys
from time import sleep
from opensimplex import OpenSimplex


class Terrain:
    def __init__(self):
        self.app = QtGui.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.setGeometry(0, 0, 1000, 1000)
        self.w.show()
        self.w.setWindowTitle('Terrain')
        self.w.setCameraPosition(distance=50, elevation=8)
        self.i = 0

        self.nsteps = 1
        self.ypoints = range(-20, 22, self.nsteps)
        self.xpoints = range(-20, 22, self.nsteps)
        self.nfaces = len(self.ypoints)
        self.tmp = OpenSimplex()
        self.offset = 0

        verts = np.array([
            [
                x, y, 1.5 * self.tmp.noise2d(x=n/5, y=m/5)
            ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
        ], dtype=np.float32)

        faces = []
        colors = []
        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append([n + yoff, yoff + n + self.nfaces, yoff + n + self.nfaces + 1])
                faces.append([n + yoff, yoff + n + 1, yoff + n + self.nfaces + 1])
                colors.append([0, 0, 0, 0])
                colors.append([0, 0, 0, 0])

        faces = np.array(faces)
        colors = np.array(colors)
        self.m1 = gl.GLMeshItem(
            vertexes=verts,
            faces=faces, faceColors=colors,
            smooth=False, drawEdges=True,
        )
        self.m1.setGLOptions('additive')
        self.w.addItem(self.m1)

    # def update(self):
    #     self.i += 1
    #     if self.i % 200 == 0:
    #         print(self.i)
    #     # self.m1.translate(0, 0, 0.001)
    #     self.m1.rotate(10, 1, 0, 0)
    def update(self):
        verts = np.array([
            [
                x, y, 1.5 * self.tmp.noise2d(x=n / 5  + self.offset, y=m / 5  + self.offset)
            ] for n, x in enumerate(self.xpoints) for m, y in enumerate(self.ypoints)
        ], dtype=np.float32)

        faces = []
        colors = []
        for m in range(self.nfaces - 1):
            yoff = m * self.nfaces
            for n in range(self.nfaces - 1):
                faces.append([n + yoff, yoff + n + self.nfaces, yoff + n + self.nfaces + 1])
                faces.append([n + yoff, yoff + n + 1, yoff + n + self.nfaces + 1])
                colors.append([0, 0.5, 0.5, 1])
                colors.append([n / self.nfaces, 1 - n / self.nfaces, m / self.nfaces, 1])

        faces = np.array(faces)
        colors = np.array(colors)

        self.m1.setMeshData(
            vertexes=verts, faces=faces, faceColors=colors
        )
        # self.offset -= 0.15

    def start(self):
        QtGui.QApplication.instance().exec_()

    def animation(self):
        timer = QtCore.QTimer()
        timer.timeout.connect(self.update)
        timer.start(10)
        self.start()
        self.update()



if __name__ == '__main__':
    t = Terrain()
    t.animation()