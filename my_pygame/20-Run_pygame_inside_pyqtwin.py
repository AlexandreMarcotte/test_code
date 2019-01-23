from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QVBoxLayout
import pygame as pg
import sys
import pyqtgraph
from my_pygame.player import Player


class ImageWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.FPS = 30
        self.BLACK = (0, 0, 0)
        self.all_sprites = None

        pg.init()
        s = pg.Surface((640, 480))
        s.fill((64, 128, 192, 224))
        pg.draw.circle(s, (255, 255, 0, 255), (200, 100), 50)

        w = s.get_width()
        h = s.get_height()
        self.data = s.get_buffer().raw
        self.image = QtGui.QImage(self.data, w, h, QtGui.QImage.Format_RGB32)

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)
        self.run()

    # def paintEvent(self,event):
    #     qp=QtGui.QPainter()
    #     qp.begin(self)
    #     qp.drawImage(0, 0, self.image)
    #     qp.end()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(self.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(self.BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100, 100, 500, 300)
        # self.layout = QVBoxLayout()
        self.layout = pyqtgraph.LayoutWidget()
        self.layout.addWidget(ImageWidget())
        self.setCentralWidget(self.layout)


app=QApplication(sys.argv)
w=MainWindow()
w.show()
app.exec_()

#
# from PyQt5.QtWidgets import *
# # from PyQt5.QtGui import QImage
# from PyQt5 import QtGui
# import my_pygame
# import sys
#
# class ImageWidget(QWidget):
#     def __init__(self,surface,parent=None):
#         super(ImageWidget,self).__init__(parent)
#         w=surface.get_width()
#         h=surface.get_height()
#         self.data=surface.get_buffer().raw
#         self.image=QtGui.QImage(self.data,w,h,QtGui.QImage.Format_RGB32)
#
#     def paintEvent(self,event):
#         qp=QtGui.QPainter()
#         qp.begin(self)
#         qp.drawImage(0,0,self.image)
#         qp.end()
#
#
# class MainWindow(QMainWindow):
#     def __init__(self,surface,parent=None):
#         super(MainWindow,self).__init__(parent)
#         self.setCentralWidget(ImageWidget(surface))
#
#
#
# my_pygame.init()
# s=my_pygame.Surface((640,480))
# s.fill((64,128,192,224))
# my_pygame.draw.circle(s,(255,255,255,255),(100,100),50)
#
# app=QApplication(sys.argv)
# w=MainWindow(s)
# w.show()
# app.exec_()
