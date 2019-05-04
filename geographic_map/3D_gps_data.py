# inspired from: https://www.geodose.com/2018/04/create-gpx-tracking-file-visualizer-python.html

import matplotlib.pyplot as plt
import time
from xml.dom import minidom
import math
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np
from sklearn.preprocessing import normalize

path = '3d_gps_data.gpx'


class GpsData:
    def __init__(self, path):
        self.path = path
        self.lons = []
        self.lats = []
        self.altitudes = []
        self.times = []

        self.create_gps_data_list()

    def read_gpx_file(self, path):
        data = open(path)
        xmldoc = minidom.parse(data)
        track = xmldoc.getElementsByTagName('trkpt')
        elevation = xmldoc.getElementsByTagName('ele')
        datetime = xmldoc.getElementsByTagName('time')
        return track, elevation, datetime

    def create_gps_data_list(self):
        track, elevation, datetime = self.read_gpx_file(self.path)
        N_TRACK = len(track)
        for track_no in range(N_TRACK):
            lon, lat = (track[track_no].attributes['lon'].value,
                        track[track_no].attributes['lat'].value)
            elev = elevation[track_no].firstChild.nodeValue
            self.lons.append(float(lon))
            self.lats.append(float(lat))
            self.altitudes.append(float(elev))
            self.parsing_time_element(datetime, track_no)

    def parsing_time_element(self, datetime, track_no):
        dt = datetime[track_no].firstChild.nodeValue
        time_split = dt.split('T')
        hms_split = time_split[1].split(':')
        time_h = int(hms_split[0])
        time_m = int(hms_split[1])
        time_s = float(hms_split[2].split('Z')[0])
        total_second = time_h * 3600 + time_m * 60 + time_s
        self.times.append(total_second)


gps_data = GpsData(path)
track_pos = []
sizes = []
colors = []

for lat, lon, alt in zip(gps_data.lats, gps_data.lons, gps_data.altitudes):
    track_pos.append([lat, lon, alt/2])
    print(lat, lon, alt)
    sizes.append(0.4)
    colors.append([0.0, 1.0, 0.0, 0.9])

def reshape_to_view(list):
    """list: list that you want to reshape to the right size to be view
       shape: The last dimension of the list"""
    arr = np.array(list)
    return arr.reshape(arr.shape[0], arr.shape[1])

def normalize(arr):
    arr -= arr.min()
    arr / arr.max()


track_pos = reshape_to_view(track_pos)
print(track_pos.shape)
colors = reshape_to_view(colors)
print(colors.shape)
sizes = np.array(sizes)
print(sizes.shape)

app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()
# g = gl.GLGridItem()
# w.addItem(g)

scatters = gl.GLScatterPlotItem(
        pos=track_pos, size=sizes, color=colors, pxMode=False)
w.addItem(scatters)


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
