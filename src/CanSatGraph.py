from PyQt5 import QtWidgets, QtCore, uic # TODO these are unneeded now?
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg

# There used to be a class instead of two functions here.
# The reason I changed it is that there is a rendering problem
# that only arises when we use a class derived from QWidget.
# It is best left alone until if / when someone more experienced with
# QT comes along. ag, 29-02-2020 00:11

def createGraph(name): #, data):

    graph = pg.PlotWidget()
    graph.setTitle(name)

    x = [] #data["MISSION_TIME"]
    y = [] #data[name]

    graph.setBackground('w')

    pen = pg.mkPen(color=(255, 0, 0))

    data_line = graph.plot(x, y, pen=pen)

    return (graph, data_line)


def updateGraph(name, line, data):
    x = data["MISSION_TIME"]
    y = data[name]

    line.setData(x, y)  # Update the data.
