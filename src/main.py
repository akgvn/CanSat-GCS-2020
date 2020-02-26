#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Şimdilik test için:
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout
from pyqtgraph import PlotWidget, plot

import sys  # We need sys so that we can pass argv to QApplication
import os
from GraphGrid import GraphGrid

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = GraphGrid()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
