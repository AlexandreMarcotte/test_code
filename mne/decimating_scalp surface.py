# Authors: Denis Engemann <denis.engemann@gmail.com>
#          Alexandre Gramfort <alexandre.gramfort@telecom-paristech.fr>
#
# License: BSD (3-clause)

import mne
from mne.surface import decimate_surface  # noqa
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore, QtGui

print(__doc__)

path = mne.datasets.sample.data_path()
surf = mne.read_bem_surfaces(path + '/subjects/sample/bem/sample-head.fif')[0]

points, triangles = surf['rr'], surf['tris']

# reduce to 30000 triangles:
points_dec, triangles_dec = decimate_surface(points, triangles,
                                             n_triangles=30000)

from mayavi import mlab  # noqa

head_col = (0.95, 0.83, 0.83)  # light pink

p, t = points_dec, triangles_dec



w = gl.GLViewWidget()
w.setGeometry(0, 0, 1000, 1000)
w.setWindowTitle('Terrain')
w.setCameraPosition(distance=50, elevation=8)

# s = gl.GLScatterPlotItem(pos=p)
mesh_data = gl.MeshData(p, t)
mesh_item = gl.GLMeshItem(
    meshdata=mesh_data, computeNormals=True, shader='viewNormalColor',
    glOptions='translucent')
# mesh_item.translate(i*0.2, j*0.3, 0)
mesh_item.setColor([0, 0, 1, 0.6])
# s.setData(=p)
w.addItem(mesh_item)
w.show()
# mlab.triangular_mesh(p[:, 0], p[:, 1], p[:, 2], t, color=head_col)
# mlab.showif __name__ == '__main__':
if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()()