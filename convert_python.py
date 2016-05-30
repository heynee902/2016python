# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convert.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(640, 480)
        self.M_posterFrame = QtWidgets.QFrame(Dialog)
        self.M_posterFrame.setGeometry(QtCore.QRect(280, 20, 171, 211))
        self.M_posterFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.M_posterFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.M_posterFrame.setObjectName("M_posterFrame")
        self.BO_listView = QtWidgets.QListView(Dialog)
        self.BO_listView.setGeometry(QtCore.QRect(10, 50, 256, 381))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(14)
        self.BO_listView.setFont(font)
        self.BO_listView.setObjectName("BO_listView")
        self.M_data2 = QtWidgets.QListView(Dialog)
        self.M_data2.setGeometry(QtCore.QRect(280, 240, 341, 192))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.M_data2.setFont(font)
        self.M_data2.setObjectName("M_data2")
        self.M_data1 = QtWidgets.QListView(Dialog)
        self.M_data1.setGeometry(QtCore.QRect(460, 20, 161, 211))
        font = QtGui.QFont()
        font.setFamily("1훈막대연필 R")
        font.setPointSize(14)
        self.M_data1.setFont(font)
        self.M_data1.setObjectName("M_data1")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 440, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 440, 171, 20))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 20, 171, 20))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 440, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "영화 상세정보 검색"))
        self.pushButton_2.setText(_translate("Dialog", "Search"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "날짜 입력(yyyymmdd)"))
        self.pushButton_3.setText(_translate("Dialog", "Exit"))

