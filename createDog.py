# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creatdog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from breedingCombos import *
from dogUI import *


class Ui_CreateDog(object):
    def setupUi(self, CreateDog):
        CreateDog.setObjectName("CreateDog")
        CreateDog.resize(379, 449)
        self.centralwidget = QtWidgets.QWidget(CreateDog)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 359, 428))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_25 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_3.addWidget(self.label_25)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.fileBrowser)
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.comboBox_6 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_6)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.comboBox_7 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_6.addWidget(self.comboBox_7)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.comboBox_10 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_10)
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.comboBox_11 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_11)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_13.addWidget(self.label_21)
        self.comboBox_20 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_20.setObjectName("comboBox_20")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_20)
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_13.addWidget(self.label_22)
        self.comboBox_21 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_21)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.comboBox_8 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_8)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_7.addWidget(self.label_10)
        self.comboBox_9 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_9)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.comboBox_5 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.comboBox_14 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_14.setObjectName("comboBox_14")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_14)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.comboBox_15 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_15)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_14.addWidget(self.label_23)
        self.comboBox_22 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.horizontalLayout_14.addWidget(self.comboBox_22)
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_14.addWidget(self.label_24)
        self.comboBox_23 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_23.setObjectName("comboBox_23")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.horizontalLayout_14.addWidget(self.comboBox_23)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_12.addWidget(self.label_19)
        self.comboBox_18 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_18.setObjectName("comboBox_18")
        self.comboBox_18.addItem("")
        self.comboBox_18.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_18)
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_12.addWidget(self.label_20)
        self.comboBox_19 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_19.setObjectName("comboBox_19")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_19)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_11.addWidget(self.label_17)
        self.comboBox_16 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_16.setObjectName("comboBox_16")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_16)
        self.label_18 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.comboBox_17 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_17)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_9.addWidget(self.label_13)
        self.comboBox_12 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_12)
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_9.addWidget(self.label_14)
        self.comboBox_13 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_13)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_15.addWidget(self.pushButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.newDog)
        self.horizontalLayout_15.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        #CreateDog.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateDog)
        QtCore.QMetaObject.connectSlotsByName(CreateDog)

    def retranslateUi(self, CreateDog):
        _translate = QtCore.QCoreApplication.translate
        CreateDog.setWindowTitle(_translate("CreateDog", "Create Dog"))
        self.label.setText(_translate("CreateDog", "Name"))
        self.label_2.setText(_translate("CreateDog", "Gender"))
        self.comboBox.setItemText(0, _translate("CreateDog", "Male"))
        self.comboBox.setItemText(1, _translate("CreateDog", "Female"))
        self.label_25.setText(_translate("CreateDog", "Picture"))
        self.pushButton.setText(_translate("CreateDog", "Browse"))
        self.label_7.setText(_translate("CreateDog", "A Locus 1"))
        self.comboBox_6.setItemText(0, _translate("CreateDog", "ay"))
        self.comboBox_6.setItemText(1, _translate("CreateDog", "at"))
        self.label_8.setText(_translate("CreateDog", "A Locus 2"))
        self.comboBox_7.setItemText(0, _translate("CreateDog", "ay"))
        self.comboBox_7.setItemText(1, _translate("CreateDog", "at"))
        self.label_11.setText(_translate("CreateDog", "B Locus 1"))
        self.comboBox_10.setItemText(0, _translate("CreateDog", "B"))
        self.comboBox_10.setItemText(1, _translate("CreateDog", "b"))
        self.label_12.setText(_translate("CreateDog", "B Locus 2"))
        self.comboBox_11.setItemText(0, _translate("CreateDog", "B"))
        self.comboBox_11.setItemText(1, _translate("CreateDog", "b"))
        self.label_21.setText(_translate("CreateDog", "C Locus 1"))
        self.comboBox_20.setItemText(0, _translate("CreateDog", "C"))
        self.comboBox_20.setItemText(1, _translate("CreateDog", "c"))
        self.label_22.setText(_translate("CreateDog", "C Locus 2"))
        self.comboBox_21.setItemText(0, _translate("CreateDog", "C"))
        self.comboBox_21.setItemText(1, _translate("CreateDog", "c"))
        self.label_9.setText(_translate("CreateDog", "D Locus 1"))
        self.comboBox_8.setItemText(0, _translate("CreateDog", "D"))
        self.comboBox_8.setItemText(1, _translate("CreateDog", "d"))
        self.label_10.setText(_translate("CreateDog", "D Locus 2"))
        self.comboBox_9.setItemText(0, _translate("CreateDog", "D"))
        self.comboBox_9.setItemText(1, _translate("CreateDog", "d"))
        self.label_3.setText(_translate("CreateDog", "E Locus 1"))
        self.comboBox_2.setItemText(0, _translate("CreateDog", "E"))
        self.comboBox_2.setItemText(1, _translate("CreateDog", "e"))
        self.label_4.setText(_translate("CreateDog", "E Locus 2"))
        self.comboBox_3.setItemText(0, _translate("CreateDog", "E"))
        self.comboBox_3.setItemText(1, _translate("CreateDog", "e"))
        self.label_5.setText(_translate("CreateDog", "K Locus 1"))
        self.comboBox_4.setItemText(0, _translate("CreateDog", "ky"))
        self.comboBox_4.setItemText(1, _translate("CreateDog", "kt"))
        self.label_6.setText(_translate("CreateDog", "K Locus 2"))
        self.comboBox_5.setItemText(0, _translate("CreateDog", "ky"))
        self.comboBox_5.setItemText(1, _translate("CreateDog", "kt"))
        self.label_15.setText(_translate("CreateDog", "M Locus 1"))
        self.comboBox_14.setItemText(0, _translate("CreateDog", "M"))
        self.comboBox_14.setItemText(1, _translate("CreateDog", "m"))
        self.label_16.setText(_translate("CreateDog", "M Locus 2"))
        self.comboBox_15.setItemText(0, _translate("CreateDog", "M"))
        self.comboBox_15.setItemText(1, _translate("CreateDog", "m"))
        self.label_23.setText(_translate("CreateDog", "S Locus 1"))
        self.comboBox_22.setItemText(0, _translate("CreateDog", "S"))
        self.comboBox_22.setItemText(1, _translate("CreateDog", "s"))
        self.label_24.setText(_translate("CreateDog", "S Locus 2"))
        self.comboBox_23.setItemText(0, _translate("CreateDog", "S"))
        self.comboBox_23.setItemText(1, _translate("CreateDog", "s"))
        self.label_19.setText(_translate("CreateDog", "Coat Length 1"))
        self.comboBox_18.setItemText(0, _translate("CreateDog", "T"))
        self.comboBox_18.setItemText(1, _translate("CreateDog", "G"))
        self.label_20.setText(_translate("CreateDog", "Coat Length 2"))
        self.comboBox_19.setItemText(0, _translate("CreateDog", "T"))
        self.comboBox_19.setItemText(1, _translate("CreateDog", "G"))
        self.label_17.setText(_translate("CreateDog", "Furnishings 1"))
        self.comboBox_16.setItemText(0, _translate("CreateDog", "F"))
        self.comboBox_16.setItemText(1, _translate("CreateDog", "l"))
        self.label_18.setText(_translate("CreateDog", "Furnishings 2"))
        self.comboBox_17.setItemText(0, _translate("CreateDog", "F"))
        self.comboBox_17.setItemText(1, _translate("CreateDog", "l"))
        self.label_13.setText(_translate("CreateDog", "Saddle Tan 1"))
        self.comboBox_12.setItemText(0, _translate("CreateDog", "N"))
        self.comboBox_12.setItemText(1, _translate("CreateDog", "I"))
        self.label_14.setText(_translate("CreateDog", "Saddle Tan 2"))
        self.comboBox_13.setItemText(0, _translate("CreateDog", "N"))
        self.comboBox_13.setItemText(1, _translate("CreateDog", "I"))
        self.pushButton_3.setText(_translate("CreateDog", "Cancel"))
        self.pushButton_2.setText(_translate("CreateDog", "Create Dog!"))

    def readDogs(self):
        try:
            with open('dogText.txt', 'rb') as file:
                Dogs = pickle.load(file)
            return Dogs
        except:
            Dogs = {}
            return Dogs

    def writeDogs(self, Dogs):
        with open('dogText.txt', 'wb') as file:
            file.write(pickle.dumps(Dogs))

    def fileBrowser(self):
        options = QFileDialog.Options()
        self.dialog = QFileDialog()
        self.dialog.setOptions(options)
        self.path, __ = QFileDialog.getOpenFileName(self.dialog, "Select Directory")

        if self.path:
            #If Windows, change the separator
            if self.path == 'C:\\':
                self.path = self.path.replace('/', '\\')
                self.lineEdit_2.setText(self.path)
                #os.chdir(self.path)
                return self.path
            # if Linux-based
            else:
                self.lineEdit_2.setText(self.path)
                #os.chdir(self.path)
                return self.path
        else:
            self.lineEdit_2.setText(self.path)
            return ""

    def newDog(self):
        Dogs = self.readDogs()
        name = self.lineEdit.text()
        gender = str(self.comboBox.currentText())
        wire1 = str(self.comboBox_16.currentText())
        coat1 = str(self.comboBox_18.currentText())
        cream1 = str(self.comboBox_2.currentText())
        black1 = str(self.comboBox_4.currentText())
        red1 = str(self.comboBox_6.currentText())
        blue1 = str(self.comboBox_8.currentText())
        base1 = str(self.comboBox_10.currentText())
        saddle1 = str(self.comboBox_12.currentText())
        dapple1 = str(self.comboBox_14.currentText())
        wire2 = str(self.comboBox_17.currentText())
        coat2 = str(self.comboBox_19.currentText())
        cream2 = str(self.comboBox_3.currentText())
        black2 = str(self.comboBox_5.currentText())
        red2 = str(self.comboBox_7.currentText())
        blue2 = str(self.comboBox_9.currentText())
        base2 = str(self.comboBox_11.currentText())
        saddle2 = str(self.comboBox_13.currentText())
        dapple2 = str(self.comboBox_15.currentText())
        pied1 = str(self.comboBox_22.currentText())
        pied2 = str(self.comboBox_23.currentText())
        coat = ''
        color = ''
        dapple = ''
        piebald = ''
        picture = self.lineEdit_2.text()
        Dogs[name] = dog(name,gender, wire1, wire2, coat1, coat2, cream1, cream2, black1, black2, red1, red2, blue1, blue2, base1, base2, saddle1, saddle2, dapple1, dapple2, pied1, pied2, picture)
        self.writeDogs(Dogs)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    createDog = QtWidgets.QWidget()
    ui = Ui_CreateDog()
    ui.setupUi(createDog)
    createDog.show()
    sys.exit(app.exec_())