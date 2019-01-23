import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
from random import randint

class GuitarHero(object):
    def __init__(self):
        # Variables
        self.N_ACTION = 4
        self.actions = []
        self.all_types = ['Left PINCH', 'Left CLOSE', 'Right PINCH', 'Right CLOSE']
        # How to read the action_order that is planned:
        # [first batch, _ ], [second batch, _ ], [third batch, _ ] ...
        # [ _, fifth batch], [ _, sixth batch] ...
        # The number tells the number of this type to spawn in the curent batch

        # Every item needs to have the same number of number in its list
        self.action_order = {'Left PINCH': [5, 5], 'Left CLOSE': [4, 4],
                             'Right PINCH': [3, 3], 'Right CLOSE': [2, 2]}
        self.next_action = []
        self.action_itt = 0
        self.init_action_order()
        # init
        self.init_graph()

    def init_action_order(self):
        for n in range(len(self.action_order['Left PINCH'])):
            for action_name, num in self.action_order.items():
                for _ in range(num[n]):
                    self.next_action.append(action_name)

    def init_graph(self):
        self.plot = pg.plot()
        self.plot.setYRange(0, 20)
        self.plot.setXRange(0, 20)
        self.plot.plotItem.hideAxis('bottom')
        self.plot.plotItem.hideAxis('left')
        # Vertical and horizontal delineation lines
        vLine = pg.InfiniteLine(angle=90, pos=10, movable=False)
        hLine = pg.InfiniteLine(angle=0, pos=3, movable=False)
        self.plot.addItem(vLine, ignoreBounds=True)
        self.plot.addItem(hLine, ignoreBounds=True)

    def update_spawn(self):
        type = self.next_action[self.action_itt]
        # Create a new action:
        action = Action(action_txt=type, wait_txt='WAIT...', pos=18, type=type)
        # Plot this new action
        self.plot.addItem(action.plot_obj)
        # Add it to the list of actions
        self.actions.append(action)
        # Incremente the action_itt so that we have the next action planified next
        self.action_itt += 1

    def update_plot(self):
        for action in self.actions:
            # update the listed position of the action
            action.pos -= 0.08
            # If the action text went is bellow the activation line
            if 2 <= action.pos <= 3:
                action.activate_html()
            # update the position of the action
            action.plot_obj.setPos(action.column, action.pos)
            # If the action is about to get out of the screen remove it
            if len(self.actions) > 5:
                self.plot.removeItem(self.actions[0].plot_obj)
                self.actions.pop(0)


class Action(object):
    def __init__(self, action_txt, wait_txt, pos, type, color='#FF0'):
        self.pos = pos
        self.type_dict = {'Left PINCH': 0, 'Left CLOSE': 1,
                          'Right PINCH': 2, 'Right CLOSE': 3}
        self.type_num = self.type_dict[type]
        self.column = 5 * self.type_num + 2.5
        self.pos = pos
        self.action_txt = action_txt
        self.wait_txt = wait_txt
        self.color = color
        self.plot_obj = None

        self.init_action()

    def init_action(self):
        self.plot_obj = pg.TextItem(anchor=(0.5, 1), angle=0,
                                    border='w', fill=(0, 0, 255, 100))
        self.action_html = f"""<div style="text-align: center">
                               <span style="color: #FFF;">{self.action_txt}
                               </span><br><span style="color: {self.color};
                               font-size: 14pt;">{self.wait_txt}</span></div>"""
        self.plot_obj.setHtml(self.action_html)
        self.plot_obj.setPos(self.column, self.pos)

    def activate_html(self):
        """Change the color  and text of the action text to indicate it's
           activation"""
        self.color = '#0FF'
        self.wait_txt = 'NOW!'
        self.html = f"""<div style="text-align: center">
                        <span style="color: #FFF;">{self.action_txt}
                        </span><br><span style="color: {self.color};
                        font-size: 16pt;">{self.wait_txt}</span></div>"""
        self.plot_obj.setHtml(self.html)


def main():
    guitar_hero = GuitarHero()

    spawn_timer = QtCore.QTimer()
    spawn_timer.timeout.connect(guitar_hero.update_spawn)
    spawn_timer.start(1000)

    plot_timer = QtCore.QTimer()
    plot_timer.timeout.connect(guitar_hero.update_plot)
    plot_timer.start(20)

    QtGui.QApplication.instance().exec_()

if __name__ == '__main__':
    main()


