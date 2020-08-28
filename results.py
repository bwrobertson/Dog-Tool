# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from breedingCombos import *
from dogUI import *


class Ui_BreedingResults(object):
    def setupUi(self, BreedingResults):
        BreedingResults.setObjectName("BreedingResults")
        BreedingResults.resize(1386, 1008)
        self.centralwidget = QtWidgets.QWidget(BreedingResults)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 1371, 931))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        pixmap = QPixmap('graphColors.jpg')
        self.label.setPixmap(pixmap)
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        pixmap = QPixmap('graphCoats.jpg')
        self.label_2.setPixmap(pixmap)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        pixmap = QPixmap('graphPiebald.jpg')
        self.label_3.setPixmap(pixmap)
        self.horizontalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        pixmap = QPixmap('graphDapple.jpg')
        self.label_4.setPixmap(pixmap)
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        #BreedingResults.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BreedingResults)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 703, 21))
        self.menubar.setObjectName("menubar")
        #BreedingResults.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BreedingResults)
        self.statusbar.setObjectName("statusbar")
        #BreedingResults.setStatusBar(self.statusbar)

        self.retranslateUi(BreedingResults)
        QtCore.QMetaObject.connectSlotsByName(BreedingResults)

    def retranslateUi(self, BreedingResults):
        _translate = QtCore.QCoreApplication.translate
        BreedingResults.setWindowTitle(_translate("BreedingResults", "Breeding Results"))
        self.label_5.setText(_translate("BreedingResults", "Breeding Results"))
        self.pushButton.setText(_translate("BreedingResults", "Ok"))


    def displayResults(self):
        pixmap = QPixmap('graphColors.jpg')
        self.label.setPixmap(pixmap)
        pixmap = QPixmap('graphCoats.jpg')
        self.label_2.setPixmap(pixmap)
        pixmap = QPixmap('graphPiebald.jpg')
        self.label_3.setPixmap(pixmap)
        pixmap = QPixmap('graphDapple.jpg')
        self.label_4.setPixmap(pixmap)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    results = QtWidgets.QWidget()
    ui = Ui_BreedingResults()
    ui.setupUi(results)
    results.show()
    sys.exit(app.exec_())
