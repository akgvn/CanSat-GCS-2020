from PyQt5 import QtWidgets, QtCore, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
# from random import randint
from ConnectionClass import SerialBridge
from CanSatGraph import *
from GraphGrid import GraphGrid

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.bridge = SerialBridge("/dev/ttyACM0", 9600)
        self.graph_data = self.bridge.getDictionary()

        self.graphWidget = GraphGrid()
        self.graphWidget.show()
        self.setCentralWidget(self.graphWidget)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.graph_data = self.bridge.getDictionary()
        self.graphWidget.update_plots(self.graph_data)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
