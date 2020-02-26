from PyQt5 import QtWidgets
import pyqtgraph as pg

class GraphGrid(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initGrid()

    def initGrid(self):
        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)

        self.graphWidget0 = pg.PlotWidget()
        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget2 = pg.PlotWidget()
        self.graphWidget3 = pg.PlotWidget()
        self.graphWidget4 = pg.PlotWidget()

        self.grid.addWidget(self.graphWidget0, 1, 0)
        self.grid.addWidget(self.graphWidget1, 1, 1)
        self.grid.addWidget(self.graphWidget2, 2, 0)
        self.grid.addWidget(self.graphWidget3, 2, 1)
        self.grid.addWidget(self.graphWidget4, 3, 0)

        print("Here")
        self.setLayout(self.grid)

        # self.setCentralWidget(self.graphWidget)

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45]

        # plot data: x, y values
        self.graphWidget0.plot(hour, temperature)
        self.graphWidget1.plot(hour, temperature)
        self.graphWidget2.plot(hour, temperature)
        self.graphWidget3.plot(hour, temperature)
        self.graphWidget4.plot(hour, temperature)
