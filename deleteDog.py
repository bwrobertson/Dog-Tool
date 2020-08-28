# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteDog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from dogUI import *


class Ui_DeleteDog(object):
    def setupUi(self, DeleteDog):
        DeleteDog.setObjectName("DeleteDog")
        DeleteDog.resize(275, 526)
        self.centralwidget = QtWidgets.QWidget(DeleteDog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 15, 253, 469))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.graphicsView = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        pixmap = QPixmap('basic.jpg')
        self.graphicsView.setPixmap(pixmap)
        self.verticalLayout.addWidget(self.graphicsView)
        self.listWidget = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_15.addWidget(self.pushButton_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.removeDog)
        self.horizontalLayout_15.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        #DeleteDog.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeleteDog)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 275, 21))
        self.menubar.setObjectName("menubar")
        #DeleteDog.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DeleteDog)
        self.statusbar.setObjectName("statusbar")
        #DeleteDog.setStatusBar(self.statusbar)
        self.listWidget.clicked.connect(self.dogClicked)
        self.retranslateUi(DeleteDog)
        QtCore.QMetaObject.connectSlotsByName(DeleteDog)

    def retranslateUi(self, DeleteDog):
        _translate = QtCore.QCoreApplication.translate
        self.setupTree()
        DeleteDog.setWindowTitle(_translate("DeleteDog", "Delete Dog"))
        self.label.setText(_translate("DeleteDog", "Dogs"))
        self.pushButton_3.setText(_translate("DeleteDog", "Cancel"))
        self.pushButton_2.setText(_translate("DeleteDog", "Delete"))

    def removeDog(self):
        Dogs = self.readDogs()
        _translate = QtCore.QCoreApplication.translate
        item = self.listWidget.currentItem()
        currentDog = Dogs[item.text()].name
        del Dogs[currentDog]
        self.writeDogs(Dogs)
        self.listWidget.clear()


    def writeDogs(self, Dogs):
        with open('dogText.txt', 'wb') as file:
            file.write(pickle.dumps(Dogs))


    def readDogs(self):
        try:
            with open('dogText.txt', 'rb') as file:
                Dogs = pickle.load(file)
            return Dogs
        except:
            Dogs = {}
            return Dogs

    def dogClicked(self):
        Dogs = self.readDogs()
        _translate = QtCore.QCoreApplication.translate
        item = self.listWidget.currentItem()
        try:
            currentDog = Dogs[item.text()]
            picture = currentDog.picture
            pixmap = QPixmap(picture)
            self.graphicsView.setPixmap(pixmap)
        except:
            pass

    def writeDogs(self, Dogs):
        with open('dogText.txt', 'wb') as file:
            file.write(pickle.dumps(Dogs))

    def setupTree(self):
        Dogs = self.readDogs()
        #print(Dogs['Eevee'].name)
        _translate = QtCore.QCoreApplication.translate
        x=0
        for pup in Dogs:
            self.listWidget.addItem(QtWidgets.QListWidgetItem())
            item = self.listWidget.item(x)
                #item.setCheckState(QtCore.Qt.Unchecked)
            if not item:
                continue
            item.setText(_translate('DogBreeder', Dogs[pup].name))
            x+=1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteDog = QtWidgets.QWidget()
    ui = Ui_DeleteDog()
    ui.setupUi(DeleteDog)
    DeleteDog.show()
    sys.exit(app.exec_())
