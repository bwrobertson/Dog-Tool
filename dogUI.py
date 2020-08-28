# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dogUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from breedingCombos import *


class Ui_DogBreeder(object):
    def setupUi(self, DogBreeder):
        DogBreeder.setObjectName("DogBreeder")
        DogBreeder.resize(863, 600)
        self.centralwidget = QtWidgets.QWidget(DogBreeder)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 40, 681, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.graphicsView = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        pixmap = QPixmap('basic.jpg')
        self.graphicsView.setPixmap(pixmap)

        self.verticalLayout.addWidget(self.graphicsView)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.breedDogs)
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")

        self.verticalLayout_2.addWidget(self.pushButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.graphicsView_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.graphicsView_2.setPixmap(pixmap)

        self.verticalLayout_3.addWidget(self.graphicsView_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        #DogBreeder.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DogBreeder)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 21))
        self.menubar.setObjectName("menubar")
        #DogBreeder.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DogBreeder)
        self.statusbar.setObjectName("statusbar")
        #DogBreeder.setStatusBar(self.statusbar)

        self.retranslateUi(DogBreeder)
        self.listWidget.clicked.connect(self.damClicked)
        self.listWidget_2.clicked.connect(self.sireClicked)
        QtCore.QMetaObject.connectSlotsByName(DogBreeder)

    def retranslateUi(self, DogBreeder):
        _translate = QtCore.QCoreApplication.translate
        self.setupTree()
        DogBreeder.setWindowTitle(_translate("DogBreeder", "DogBreeder"))
        self.label.setText(_translate("DogBreeder", "Dams"))
        self.pushButton.setText(_translate("DogBreeder", "Breed"))
        self.pushButton_3.setText(_translate("DogBreeder", "Add Dog"))
        self.pushButton_4.setText(_translate("DogBreeder", "Delete Dog"))
        self.label_2.setText(_translate("DogBreeder", "Sires"))

    def ReadDogs(self):
        try:
            with open('dogText.txt', 'rb') as file:
                Dogs = pickle.load(file)
            return Dogs
        except:
            Dogs = {}
            return Dogs

    def damClicked(self):
        Dogs = self.ReadDogs()
        _translate = QtCore.QCoreApplication.translate
        item = self.listWidget.currentItem()
        currentDog = Dogs[item.text()]
        picture = currentDog.picture
        pixmap = QPixmap(picture)
        self.graphicsView.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())
        #pic = QtGui.QPixmap(picture)
        #self.graphicsView.addItem(QtGui.QGraphicsPixmapItem(pic))

    def sireClicked(self):
        Dogs = self.ReadDogs()
        _translate = QtCore.QCoreApplication.translate
        item = self.listWidget_2.currentItem()
        currentDog = Dogs[item.text()]
        picture = currentDog.picture
        pixmap = QPixmap(picture)
        self.graphicsView_2.setPixmap(pixmap)
        #self.resize(pixmap.width(), pixmap.height())
        #pic = QtGui.QPixmap(picture)
        #self.graphicsView.addItem(QtGui.QGraphicsPixmapItem(pic))

    def setupTree(self):
        Dogs = self.ReadDogs()
        #print(Dogs['eevee'].coat)
        _translate = QtCore.QCoreApplication.translate
        xx=0
        xy=0
        for pup in Dogs:
            if(Dogs[pup].gender == 'Female'):
                self.listWidget.addItem(QtWidgets.QListWidgetItem())
                item = self.listWidget.item(xx)
                #item.setCheckState(QtCore.Qt.Unchecked)
                if not item:
                    continue
                item.setText(_translate('DogBreeder', Dogs[pup].name))
                xx+=1
            if(Dogs[pup].gender == 'Male'):
                self.listWidget_2.addItem(QtWidgets.QListWidgetItem())
                item = self.listWidget_2.item(xy)
                #item.setCheckState(QtCore.Qt.Unchecked)
                if not item:
                    continue
                item.setText(_translate('DogBreeder', Dogs[pup].name))
                xy+=1

    def breedDogs(self):
        Dogs = self.ReadDogs()
        _translate = QtCore.QCoreApplication.translate
        try:
            dam = self.listWidget.currentItem()
            sire = self.listWidget_2.currentItem()
            dam = Dogs[dam.text()]
            sire = Dogs[sire.text()]
            dogBreeding(dam,sire)
        except:
            pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dogBreeder = QtWidgets.QWidget()
    ui = Ui_DogBreeder()
    ui.setupUi(dogBreeder)
    dogBreeder.show()
    sys.exit(app.exec_())
