from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QSplashScreen, QMenu, QApplication, QProgressBar, QMessageBox
from qtpy import QtCore

import sys

import qtmodern.styles
import qtmodern.windows

from dogUI import *
from createDog import *
from deleteDog import *
from results import *

class dogUIWindow(QtWidgets.QDialog, Ui_DogBreeder):
    def __init__(self, parent=None):
        super(dogUIWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Pretzel.jpg"))
        self.setupUi(self)


class createDogWindow(QtWidgets.QWidget, Ui_CreateDog):
    def __init__(self, parent=None):
        super(createDogWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Pretzel.jpg"))
        self.setupUi(self)
        #Cancel
        self.pushButton_3.clicked.connect(self.close)
        #Create
        self.pushButton_2.clicked.connect(self.close)

class deleteDogWindow(QtWidgets.QWidget, Ui_DeleteDog):
    def __init__(self, parent=None):
        super(deleteDogWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Pretzel.jpg"))
        self.setupUi(self)
        #Cancel
        self.pushButton_3.clicked.connect(self.close)
        #Delete
        self.pushButton_2.clicked.connect(self.close)

class resultsWindow(QtWidgets.QWidget, Ui_BreedingResults):
    def __init__(self, parent=None):
        super(resultsWindow, self).__init__(parent)
        self.setWindowIcon(QIcon("Pretzel.jpg"))
        self.setupUi(self)
        #Cancel
        self.pushButton.clicked.connect(self.close)



class Controller:
    def __init__(self):
        self.launchProgram()

    def launchProgram(self):
        self.dogBreeder = dogUIWindow()
        self.createDog = createDogWindow()
        self.deleteDog = deleteDogWindow()
        self.results = resultsWindow()

        #Create New Dog Button
        self.dogBreeder.pushButton_3.clicked.connect(self.createDog.show)
        #Delete Dog Button
        self.dogBreeder.pushButton_4.clicked.connect(self.deleteDog.show)
        #Refresh tree when a button that updates dogs is pressed
        self.dogBreeder.pushButton_4.clicked.connect(self.deleteDog.setupTree)
        self.createDog.pushButton_2.clicked.connect(self.dogBreeder.setupTree)

        self.deleteDog.pushButton_2.clicked.connect(self.dogBreeder.listWidget.clear)
        self.deleteDog.pushButton_2.clicked.connect(self.dogBreeder.listWidget_2.clear)
        self.deleteDog.pushButton_2.clicked.connect(self.dogBreeder.setupTree)

        self.dogBreeder.pushButton.clicked.connect(self.results.show)
        self.dogBreeder.pushButton.clicked.connect(self.results.displayResults)
        self.dogBreeder.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.light(app)
    controller = Controller()
    #controller.dogBreeder.show()
    sys.exit(app.exec_())
