from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import sys
from ConnectionClass import SerialBridge

import matplotlib
matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=4, height=3, dpi=100, name = ""):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        assert name != "", "Name can't be blank!" # TODO this is tech debt, fix this soon. - ag, 27-02-2020 15:02

        self.xdata = []
        self.ydata = []

        self.name = name

        super(MplCanvas, self).__init__(fig)


class GraphGrid(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bridge = SerialBridge(9600, "/dev/ttyACM0")
        self.graph_data = self.bridge.getDictionary()

        self.initGrid()

    def initGrid(self):

        # Grid Design:
        # 6 real-time graphs: altitude, pressure, temperature,
        # voltage, air speed, particle count. Right side of
        # the window will host a textbox with raw telemetry data.

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)

        width, height, dpi = 5, 4, 100
        self.alti_graph = MplCanvas(self, width, height, dpi, "ALTITUDE")
        self.pressure = MplCanvas(self, width, height, dpi, "PRESSURE")
        self.temp = MplCanvas(self, width, height, dpi, "TEMP")
        self.voltage = MplCanvas(self, width, height, dpi, "VOLTAGE")
        self.air_speed = MplCanvas(self, width, height, dpi, "AIR_SPEED")
        self.particle_count = MplCanvas(
            self, width, height, dpi, "PARTICLE_COUNT")

        self.update_plots()

        self.show()

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)  # in milliseconds
        self.timer.timeout.connect(self.update_plots)
        self.timer.start()

        print("Here")
        self.setLayout(self.grid)

        self.grid.addWidget(self.alti_graph, 1, 0)
        self.grid.addWidget(self.pressure, 1, 1)
        self.grid.addWidget(self.temp, 2, 0)
        self.grid.addWidget(self.voltage, 2, 1)
        self.grid.addWidget(self.air_speed, 3, 0)
        self.grid.addWidget(self.particle_count, 3, 1)

    def update_plot(self, canvas):
        # Drop off the first y element, append a new one.
        canvas.xdata = self.graph_data["MISSION_TIME"]
        canvas.ydata = self.graph_data[canvas.name]

        canvas.axes.cla()  # Clear the canvas.
        canvas.axes.plot(canvas.xdata, canvas.ydata, 'r')
        canvas.draw()  # Trigger the canvas to update and redraw.

    def update_plots(self):

        # TODO Kayhan -> getDictionary function will be updated to read data from serial such that when we call it from here it reads serial and appends to the dict first.
        self.graph_data = self.bridge.getDictionary()
        print(self.graph_data)

        self.update_plot(self.alti_graph)
        self.update_plot(self.pressure)
        self.update_plot(self.temp)
        self.update_plot(self.voltage)
        self.update_plot(self.air_speed)
        self.update_plot(self.particle_count)
