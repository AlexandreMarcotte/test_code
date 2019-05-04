import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
from random import random
import cv2
import matplotlib.pyplot as plt

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


def create_3D_volume_from_3D_np_array(arr, scale=1, translate=(0, 0, 0)):
    volume = gl.GLVolumeItem(arr, sliceDensity=5, smooth=False)
    # Translate
    volume.translate(-arr.shape[0]/2 * scale,
                     -arr.shape[1]/2 * scale,
                     -arr.shape[2]/2 * scale)
    volume.translate(*translate)
    # Scale
    # v.scale(scale, scale, scale)
    return volume


def main():
    cat_img_rgb = cv2.imread(
            '/home/alex/Documents/CODING/2019/test_code/3D/open_gl/cat.png')
    cat_img_rgba = np.concatenate(
            (cat_img_rgb,
             np.ones((cat_img_rgb.shape[0], cat_img_rgb.shape[1], 1)) * 2),
             axis=2)
    cat_img_rgba = cat_img_rgba.reshape(
            (cat_img_rgba.shape[0], cat_img_rgba.shape[1], 1, 4))
    # arr = create_random_array()

    for i in range(20):
        view.addItem(create_3D_volume_from_3D_np_array(
                cat_img_rgba, translate=(0, 0, i*40)))
    QtGui.QApplication.instance().exec_()


if __name__ == '__main__':
    main()


