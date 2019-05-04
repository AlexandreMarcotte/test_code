import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from random import random

import cv2

cat_img = cv2.imread('/home/alex/Documents/CODING/2019/test_code/3D/open_gl/cat.png')
print(cat_img)

# SEE ReadQImage() function of glVolumeItem --------------

app = QtGui.QApplication([])
view = gl.GLViewWidget()
view.setCameraPosition(distance=120, azimuth=-90)
view.show()


def create_random_array():
    arr = np.zeros((50, 50, 1, 4))
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            r = random() * 255
            g = random() * 255
            b = random() * 255
            arr[i, j, 0] = [r, g, b, 255]
    return arr


def create_3D_volume_from_3D_np_array(arr, scale=1):
    volume = gl.GLVolumeItem(arr, sliceDensity=5, smooth=False)
    # Translate
    volume.translate(-arr.shape[0]/2 * scale,
                     -arr.shape[1]/2 * scale,
                     -arr.shape[2]/2 * scale)
    # Scale
    # v.scale(scale, scale, scale)
    return volume


def update():
    arr = create_random_array()
    # Remove all items
    view.items = []
    view.addItem(create_3D_volume_from_3D_np_array(arr))

def main():
    t = QtCore.QTimer()
    t.timeout.connect(update)
    t.start(0)
    QtGui.QApplication.instance().exec_()


if __name__ == '__main__':
    main()



