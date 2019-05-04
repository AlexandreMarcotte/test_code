from PyQt5 import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy


# Non fonctionnel, comprendre mieux les événements avec l'exemple de base de
# pyqtgraph


class Grid(gl.GLGridItem):
    def __init__(
            self, size=(0, 0, 0), spacing=(0, 0, 0), translate=(0, 0, 0),
            rotate=(0, 0, 0, 0)):
        super().__init__()
        self.setSize(*size)
        self.setSpacing(*spacing)
        self.translate(*translate)
        self.rotate(*rotate)


class PlotObject(gl.GLViewWidget):
    """ Override GLViewWidget with enhanced behavior

    """
    #: Fired in update() method to synchronize listeners.
    sigUpdate = QtCore.Signal(float, float)
    App = None

    def __init__(self, app=None):
        if self.App is None:
            if app is not None:
                self.App = app
            else:
                self.App = QtGui.QApplication([])

        super().__init__()
        # Create the view
        self.setCameraPosition(distance=15000)
        self.setGeometry(0, 110, 1920, 1080)
        self.show()

        self.Gridxy = Grid(
                size=(6000, 2000, 3), spacing=(200, 200, 0),
                translate=(3000, 0, 0))
        self.Gridyz = Grid(
                size=(1800, 2000, 3), spacing=(200, 200, 0),
                translate=(900, 0, 0), rotate=(-90, 0, 1, 0))
        self.Gridxz = Grid(
            size=(6000, 2000, 3), spacing=(200, 200, 0),
            translate=(3000, -1000, 0), rotate=(-90, 1, 0, 0))

        self.Poss = []

        self.Plot = gl.GLScatterPlotItem()
        self.addItem(self.Plot)
        self.addItem(self.Gridxy)
        self.addItem(self.Gridyz)
        self.addItem(self.Gridxz)

        self.Axes = gl.GLAxisItem()
        self.addItem(self.Axes)
        self._downpos = []

        # self.update_graph().connect(self.rayCast)
        self.sigUpdate.connect(self.rayCast)
        self.setWindowTitle('Center of Gravity of Parts')

    def mousePressEvent(self, ev):
        """ Store the position of the mouse press for later use.

        """
        super(PlotObject, self).mousePressEvent(ev)
        self._downpos = self.mousePos

    def mouseReleaseEvent(self, ev):
        """ Allow for single click to move and right click for context menu.

        Also emits a sigUpdate to refresh listeners.
        """
        super(PlotObject, self).mouseReleaseEvent(ev)
        if self._downpos == ev.pos():
            x = ev.pos().x()
            y = ev.pos().y()
            if ev.button() == 2 :
                self.mPosition()
            elif ev.button() == 1:
                x = x - self.width() / 2
                y = y - self.height() / 2
                #self.pan(-x, -y, 0, relative=True)
                print(self.opts['center'])
                print(x,y)
        self._prev_zoom_pos = None
        self._prev_pan_pos = None

    def mouseMoveEvent(self, ev):
        """ Allow Shift to Move and Ctrl to Pan.

        """
        shift = ev.modifiers() & QtCore.Qt.ShiftModifier
        ctrl = ev.modifiers() & QtCore.Qt.ControlModifier
        if shift:
            y = ev.pos().y()
            if not hasattr(self, '_prev_zoom_pos') or not self._prev_zoom_pos:
                self._prev_zoom_pos = y
                return
            dy = y - self._prev_zoom_pos
            def delta():
                return -dy * 5
            ev.delta = delta
            self._prev_zoom_pos = y
            self.wheelEvent(ev)
        elif ctrl:
            pos = ev.pos().x(), ev.pos().y()
            if not hasattr(self, '_prev_pan_pos') or not self._prev_pan_pos:
                self._prev_pan_pos = pos
                return
            dx = pos[0] - self._prev_pan_pos[0]
            dy = pos[1] - self._prev_pan_pos[1]
            self.pan(dx, dy, 0, relative=True)
            self._prev_pan_pos = pos
        else:
            super(PlotObject, self).mouseMoveEvent(ev)

    def plotGLPlot(self, objs):
        poss = numpy.array([0, 0, 0])
        self.Poss = []
        self.GlobalInds = []
        weights = numpy.array(0, dtype=float)
        def pswc (x) : return 10 * x**0.25 #pseudoweight calculation with exponential scaling
        for obj in objs:
            for i,cogs in enumerate(obj.CoG):
                for cog in cogs:
                    #cog[1] = 0
                    if obj.PieceWeight[i]:
                        poss = numpy.vstack([poss,numpy.asarray(cog.T)])
                        self.Poss.append(numpy.matrix(cog.T)) # for picking stuff
                        self.GlobalInds.append(obj.Index[i])
                        pw = pswc(obj.PieceWeight[i])
                        weights = numpy.append(weights, pw)

        maxw = max(weights)
        threshold = numpy.mean(weights)
        self.Colors = numpy.empty([len(weights),4])
        for i, pw in enumerate(weights):
            if pw <= threshold:
                c = pw / maxw
                self.Colors[i] = numpy.array([c,1,0,0.7])
            else:
                c = 1 - pw / maxw
                self.Colors[i] = numpy.array([1,c,0,0.7])

        self.removeItem(self.Plot)
        self.Plot = gl.GLScatterPlotItem()
        self.Plot.setData(pos=poss, size=weights, color=self.Colors, pxMode=False)
        self.Sizes = weights
        self.addItem(self.Plot)
        self.show()

    def mPosition(self):
        #This function is called by a mouse event
        ## Get mouse coordinates saved when the mouse is clicked( incase dragging)
        mx = self._downpos.x()
        my = self._downpos.y()
        self.Candidates = [] #Initiate a list for storing indices of picked points
        #Get height and width of 2D Viewport space
        view_w = self.width()
        view_h = self.height()
        #Convert pixel values to normalized coordinates
        x = 2.0 * mx / view_w - 1.0
        y = 1.0 - (2.0 * my / view_h)
        # Convert projection and view matrix to numpy types and inverse them
        PMi = self.projectionMatrix().inverted()[0]
        # PMi = numpy.matrix([PMi[0:4],
        #                    PMi[4:8],
        #                    PMi[8:12],
        #                    PMi[12:16]])
        VMi = self.viewMatrix().inverted()[0]
        # VMi = numpy.matrix([VMi[0:4],
        #                    VMi[4:8],
        #                    VMi[8:12],
        #                    VMi[12:16]])
        #Move to clip coordinates by chosing z= -1 and w 1 (Dont understand this part)
        # Q1: Why are we picking arbitrary -1 for z?
        ray_clip = QtGui.QVector4D(x, y, -1.0, 1.0) # get transpose for matrix multiplication
        # Q2 = Clip space should clip some of the scene depending on the zoom. How is it done? Is it implicit
        # in the transformation matrices?
        # Convert to eye space by view matrix
        ray_eye = PMi * ray_clip
        ray_eye.setZ(-1)
        ray_eye.setW(0)
        #Convert to world coordinates
        ray_world = VMi * ray_eye
        ray_world = QtGui.QVector3D(ray_world.x(), ray_world.y(), ray_world.z()) # get transpose for matrix multiplication
        ray_world.normalize()
        #ray_world = ray_world / numpy.linalg.norm(ray_world) # normalize to get the ray
        # Q3: Since we normalize this vector, does it mean the values are a b c values of a ray definition in
        # linear algebra such as z = ax+by+c
        # Now I 'll use the ray intersection with spheres. I assume every point is a sphere with a radius
        #Please see http://antongerdelan.net/opengl/raycasting.html scroll down to spehere intersection
        O = numpy.matrix(self.cameraPosition())  # camera position should be starting point of the ray
        ray_world = numpy.matrix([ray_world.x(), ray_world.y(), ray_world.z()])
        # Q4: Is this approach correct? Is starting point really the camera coordinates obtained like this?
        print(O, ray_world)
        for i, C in enumerate(self.Poss): # Iterate over all points
            OC = O - C
            b = numpy.inner(ray_world, OC)
            b = b.item(0)
            c = numpy.inner(OC, OC)
            #Q5: When the plot function is called with pxMode = False the sizes should reflect the size of point
            #dots in world coordinates. So I assumed they were the diameter of the spheres. Is this correct? Otherwise how do I reach the
            #diameter of spheres in terms of world coordinates?
            c = c.item(0) - (self.Sizes[i]/2)**2   #numpy.square((self.Sizes[i]))
            bsqr = numpy.square(b)
            if (bsqr - c) >= 0: # means intersection
                self.Candidates.append(self.GlobalInds[i])

        print(self.Candidates)

    def exec_graph(self):
        QtGui.QApplication.instance().exec_()


def main():
    plot_object = PlotObject()
    plot_object.exec_graph()

if __name__ == '__main__':
    main()

