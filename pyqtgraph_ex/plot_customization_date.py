import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
import time
from datetime import datetime
from datetime import datetime as dt

class DateAxis(pg.AxisItem):
    def tickStrings(self, values, scale, spacing):
        strns = []
        rng = max(values)-min(values)
        if rng < 3600*24:
            string = '%H:%M:%S'
            label1 = '%b %d -'
            label2 = ' %b %d, %Y'
        elif rng >= 3600*24 and rng < 3600*24*30:
            string = '%d'
            label1 = '%b - '
            label2 = '%b, %Y'
        elif rng >= 3600*24*30 and rng < 3600*24*30*24:
            string = '%b'
            label1 = '%Y -'
            label2 = ' %Y'
        elif rng >=3600*24*30*24:
            string = '%Y'
            label1 = ''
            label2 = ''
        for x in values:
            try:
                strns.append(time.strftime(string, time.localtime(x)))
            except ValueError:  # Windows can't handle dates before 1970
                strns.append('')
        try:
            label = time.strftime(
                    label1, time.localtime(min(values))) \
                  + time.strftime(label2, time.localtime(max(values)))
        except ValueError:
            label = ''
        return strns


app = pg.mkQApp()
date_axis = DateAxis(orientation='bottom')
vb = pg.ViewBox()

pw = pg.PlotWidget(
        viewBox=vb, axisItems={'bottom': date_axis}, enableMenu=False,
        title='PlotItem')


dates = [dt(2018, 1, 5), dt(2018, 3, 6)]  # Date is given by the number of second after 1970
print(dates)
dates = [datetime.timestamp(d) for d in dates]
pw.plot(x=dates, y=[1, 6], symbol='o', pen='g', label='data')
pw.show()

if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
