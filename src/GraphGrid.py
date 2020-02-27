from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from ConnectionClass import SerialBridge
import sys

class GCGraph(QtWidgets.QWidget):

    def __init__(self, name):
        super().__init__()

        self.graphWidget = pg.PlotWidget()

        self.name = name
        self.x = []
        self.y = []

        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))  # Red

        self.line = self.graphWidget.plot(self.x, self.y, pen=pen)

    def update_plot_data(self, graph_dict):
        self.x = graph_dict["MISSION_TIME"]
        self.y = graph_dict[self.name]
        
        self.line.setData(self.x, self.y)  # Update the data.


class GraphGrid(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bridge = SerialBridge("/dev/ttyACM0", 9600)
        self.graph_data = self.bridge.getDictionary()

        self.initGrid()

    def initGrid(self):

        # Grid Design:
        # 6 real-time graphs: altitude, pressure, temperature,
        # voltage, air speed, particle count. Right side of
        # the window will host a textbox with raw telemetry data.

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)

        self.alti_graph = GCGraph("ALTITUDE")
        self.pressure = GCGraph("PRESSURE")
        self.temp = GCGraph("TEMP")
        self.voltage = GCGraph("VOLTAGE")
        self.air_speed = GCGraph("AIR_SPEED")
        self.particle_count = GCGraph("PARTICLE_COUNT")

        self.update_plots()

        # Setup a timer to redraw all graphs.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)  # in milliseconds
        self.timer.timeout.connect(self.update_plots)
        self.timer.start()

        self.setLayout(self.grid)

        self.grid.addWidget(self.alti_graph, 1, 0)
        self.grid.addWidget(self.pressure, 1, 1)
        self.grid.addWidget(self.temp, 2, 0)
        self.grid.addWidget(self.voltage, 2, 1)
        self.grid.addWidget(self.air_speed, 3, 0)
        self.grid.addWidget(self.particle_count, 3, 1)

    def update_plots(self):

        # TODO Kayhan -> getDictionary function will be updated to read data from serial such that when we call it from here it reads serial and appends to the dict first.
        self.graph_data = self.bridge.getDictionary()

        self.alti_graph.update_plot_data(self.graph_data)
        self.pressure.update_plot_data(self.graph_data)
        self.temp.update_plot_data(self.graph_data)
        self.voltage.update_plot_data(self.graph_data)
        self.air_speed.update_plot_data(self.graph_data)
        self.particle_count.update_plot_data(self.graph_data)
        