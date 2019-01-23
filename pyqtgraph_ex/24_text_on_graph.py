from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg


app = QtGui.QApplication([])

win = pg.GraphicsWindow()

pg.setConfigOptions(antialias=True)

voieTT=np.ones(100)
voieTemps=np.ones(100)
for i in range(100):
    voieTT[i]=np.random.random_sample()
    voieTemps[i]=i

signemax=np.max(voieTT)
tmax=np.where(voieTT==np.max(voieTT))[0][0]

grapheTT = win.addPlot(enableMenu=False)

grapheTTVB=grapheTT.getViewBox()
grapheTT.plot(voieTemps, voieTT)
grapheTT.plot([tmax],[signemax],symbol='o',symbolSize=8)
grapheTT.showGrid(x=True, y=True)

textVmax = pg.TextItem(anchor=(0.5,1.5), border='w', fill=(0,0,255))
txt = """<div style="text-align: center"><span 
         style="color: #F1F;">Vmax=%0.1f mm/s @ %0.1f s</span></div>"""
textVmax.setHtml(txt % (np.abs(signemax), tmax))
grapheTT.addItem(textVmax)
textVmax.setPos(tmax, signemax)


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()