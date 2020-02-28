from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
from ConnectionClass import SerialBridge
from CanSatGraph import *
import sys
from random import randint


class GraphGrid(QtWidgets.QDialog):
    def __init__(self, *args, **kwargs):
        super(GraphGrid, self).__init__(*args, **kwargs)

        # Grid Design:
        # 6 real-time graphs: altitude, pressure, temperature,
        # voltage, air speed, particle count. Right side of
        # the window will host a textbox with raw telemetry data.

        self.grid = QtWidgets.QGridLayout()
        # self.grid.setSpacing(10)

        self.graphs = []
        self.data_lines = []

        self.graph_names = ["ALTITUDE", "PRESSURE", "TEMP",
                            "VOLTAGE", "AIR_SPEED", "PARTICLE_COUNT"]

        for gn in self.graph_names:
            g, d = createGraph(gn)
            self.graphs.append(g)
            self.data_lines.append(d)

        for loc in range(1, 4):
            for idx in range(len(self.graph_names)):
                self.grid.addWidget(self.graphs[idx], 1, (idx % 2))

        """
        self.grid.addWidget(self.alti_graph, 1, 0)
        self.grid.addWidget(self.pressure, 1, 1)
        self.grid.addWidget(self.temp, 2, 0)
        self.grid.addWidget(self.voltage, 2, 1)
        self.grid.addWidget(self.air_speed, 3, 0)
        self.grid.addWidget(self.particle_count, 3, 1)
        """

        self.setLayout(self.grid)

    def update_plots(self, graph_data):

        for idx in range(len(self.graph_names)):
            name = self.graph_names[idx]
            data_line = self.data_lines[idx]
            updateGraph(name, data_line, graph_data)

        """
        self.alti_graph.update(graph_data)
        self.pressure.update(graph_data)
        self.temp.update(graph_data)
        self.voltage.update(graph_data)
        self.air_speed.update(graph_data)
        self.particle_count.update(graph_data)
        """
