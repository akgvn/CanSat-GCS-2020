from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

class CanSatGraph(QtWidgets.QWidget):
    def __init__(self, name):
        super(CanSatGraph, self).__init__()

        self.name = name
        self.graph = pg.PlotWidget()
        self.graph.setTitle(name)

        self.x = [] # data["MISSION_TIME"]
        self.y = [] # data[name]

        self.graph.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graph.plot(self.x, self.y, pen=pen)

        # self.graph.show()

    def update(self, data):

        self.x = data["MISSION_TIME"]
        self.y = data[self.name]

        self.data_line.setData(self.x, self.y)  # Update the data.
