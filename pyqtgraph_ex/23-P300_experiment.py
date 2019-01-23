from pyqtgraph.Qt import QtGui
import pyqtgraph as pg
from random import randint
import sklearn.pipeline as p

p.Pipeline

app = QtGui.QApplication([])
win = pg.GraphicsWindow()

graph = win.addPlot()
graph.setXRange(-0.5, 6)
graph.setYRange(-1.5, 5.5)
graph.hideAxis('bottom')
graph.hideAxis('left')

char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_']

def update():
    rand_row = randint(0, 5)
    rand_col = randint(0, 5)
    # Add all number to the plot
    graph.clear()
    for no in range(36):
        col = no % 6
        row = no // 6
        if rand_col == col or rand_row == row:
            char_color = '#F00'
        else:
            char_color = '#00F'

        txt = pg.TextItem(fill=(0,0,0))
        html="""<span style="color: {char_color};
                 font-size: 56pt; ">
                 {p300_char}""".format(char_color=char_color, p300_char=char[no])
        txt.setHtml(html)

        graph.addItem(txt)
        txt.setPos(col, row)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(100)

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()




# old p300
# Select a new random position for the cross
# rand_h = randint(0, 5)
# rand_v = randint(0, 5)
# # Remove all widget from the previous screen
# for i in reversed(range(self.tab2.layout.count())):
#     self.tab2.layout.itemAt(i).widget().deleteLater()
# # Draw all characters
# for i, c in enumerate(self.char):
#     pos_v = i // 6
#     pos_h = i % 6
#     text = QLabel(c)
#     text.setFont(self.font)
#     # Put lighter color on the selected cross
#     if pos_h == rand_h or pos_v == rand_v:
#         color = self.LIGHT_GREY
#     else:
#         color = self.DARK_GREY
#     style = ('QLabel { color : ' + '{color}'.format(color=color) + ' }')
#     text.setStyleSheet(style)
#     self.tab2.layout.addWidget(text, pos_v + 1, pos_h, 1, 1)