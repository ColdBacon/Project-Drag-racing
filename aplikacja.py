import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.integrate import odeint

import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QDialog, QWidget, QMainWindow


class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow,self).__init__()
        loadUi(r'D:\Dokumenty\SEMESTR3\Project-Drag-racing\app.ui',self)
        self.setWindowTitle('Drag racing simulation')
        self.initUI()

    def initUI(self):
        self.simulate.clicked.connect(self.getValues)

    def getValues(self):
        slope = self.slope.text()
        print("Slope: ",slope)
        meta = self.meta.text()
        print("Meta: ", meta)
        power1 = self.power1.text()
        print("Power 1: ",power1)
        power2 = self.power2.text()
        print("Power 2: ",power2)
        mass1 = self.mass1.text()
        print("Mass 1: ",mass1)
        mass2 = self.mass2.text()
        print("Mass 2: ",mass2)
        drag1 = self.dragCo1.text()
        print("Drag coefficient 1: ",drag1)
        drag2 = self.dragCo2.text()
        print("Drag coefficient 2: ",drag2)
        area1 = self.area1.text()
        print("Cross-sectional area 1: ",area1)
        area2 = self.area2.text()
        print("Cross sectional area 2: ",area2)

        os.chdir('D:\Dokumenty\SEMESTR3\Project-Drag-racing')
        text = "python wykresiki.py "+ slope + " " + meta + " " + power1 + " " + power2 + " " + mass1 + " " + mass2 + " " + drag1 + " " + drag2 + " " + area1 + " " + area2
        os.system(text)


def app():
    my_app = QApplication(sys.argv)
    w = MyWindow()

    w.show()
    #infinite loop
    sys.exit(my_app.exec_())

app()
