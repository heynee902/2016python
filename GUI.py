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
        Dialog.resize(501, 619)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 601))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit_date = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_date.setGeometry(QtCore.QRect(10, 10, 191, 21))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setInputMask("")
        self.lineEdit_date.setText("")
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.frame_poster = QtWidgets.QFrame(self.tab)
        self.frame_poster.setGeometry(QtCore.QRect(60, 350, 141, 181))
        self.frame_poster.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_poster.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_poster.setObjectName("frame_poster")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(210, 10, 131, 25))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_Search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_Search.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_Search.setAutoRepeatDelay(300)
        self.pushButton_Search.setAutoRepeatInterval(100)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout.addWidget(self.pushButton_Search)
        self.pushButton_Exit = QtWidgets.QPushButton(self.tab)
        self.pushButton_Exit.setGeometry(QtCore.QRect(380, 540, 75, 23))
        self.pushButton_Exit.setAutoRepeat(False)
        self.pushButton_Exit.setAutoRepeatInterval(101)
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.listWidget_box = QtWidgets.QListWidget(self.tab)
        self.listWidget_box.setGeometry(QtCore.QRect(10, 100, 191, 241))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget_box.setFont(font)
        self.listWidget_box.setObjectName("listWidget_box")
        self.listWidget_audi = QtWidgets.QListWidget(self.tab)
        self.listWidget_audi.setGeometry(QtCore.QRect(210, 100, 121, 241))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget_audi.setFont(font)
        self.listWidget_audi.setObjectName("listWidget_audi")
        self.listWidget_sales = QtWidgets.QListWidget(self.tab)
        self.listWidget_sales.setGeometry(QtCore.QRect(340, 100, 121, 241))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget_sales.setFont(font)
        self.listWidget_sales.setObjectName("listWidget_sales")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 191, 51))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(0)
        self.label_2.setMidLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 121, 51))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(True)
        self.label_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(340, 40, 121, 51))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(True)
        self.label_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.listWidget_info = QtWidgets.QListWidget(self.tab)
        self.listWidget_info.setGeometry(QtCore.QRect(210, 350, 251, 181))
        self.listWidget_info.setObjectName("listWidget_info")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 350, 41, 181))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.label_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setWordWrap(True)
        self.label_5.setIndent(0)
        self.label_5.setOpenExternalLinks(False)
        self.label_5.setObjectName("label_5")
        self.lineEdit_date.raise_()
        self.frame_poster.raise_()
        self.horizontalLayoutWidget.raise_()
        self.pushButton_Exit.raise_()
        self.listWidget_box.raise_()
        self.listWidget_audi.raise_()
        self.listWidget_sales.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton_Search.raise_()
        self.pushButton_Search.raise_()
        self.listWidget_info.raise_()
        self.label_5.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(160, 430, 160, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.lineEdit_mail_PW = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_mail_PW.setGeometry(QtCore.QRect(100, 260, 281, 31))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.lineEdit_mail_PW.setFont(font)
        self.lineEdit_mail_PW.setInputMask("")
        self.lineEdit_mail_PW.setText("")
        self.lineEdit_mail_PW.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mail_PW.setObjectName("lineEdit_mail_PW")
        self.lineEdit_mail_ID = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_mail_ID.setGeometry(QtCore.QRect(100, 210, 281, 31))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.lineEdit_mail_ID.setFont(font)
        self.lineEdit_mail_ID.setInputMask("")
        self.lineEdit_mail_ID.setText("")
        self.lineEdit_mail_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mail_ID.setObjectName("lineEdit_mail_ID")
        self.lineEdit_mail_address = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_mail_address.setGeometry(QtCore.QRect(100, 310, 281, 31))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.lineEdit_mail_address.setFont(font)
        self.lineEdit_mail_address.setInputMask("")
        self.lineEdit_mail_address.setText("")
        self.lineEdit_mail_address.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mail_address.setObjectName("lineEdit_mail_address")
        self.lineEdit_mail_address_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_mail_address_2.setGeometry(QtCore.QRect(100, 360, 281, 31))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(12)
        self.lineEdit_mail_address_2.setFont(font)
        self.lineEdit_mail_address_2.setInputMask("")
        self.lineEdit_mail_address_2.setText("")
        self.lineEdit_mail_address_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_mail_address_2.setObjectName("lineEdit_mail_address_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(90, 80, 301, 81))
        font = QtGui.QFont()
        font.setFamily("1훈정글북 Regular")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_Exit.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit_date.setPlaceholderText(_translate("Dialog", "날짜 입력(yyyymmdd)"))
        self.pushButton_Search.setText(_translate("Dialog", "Search"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))
        self.label_2.setText(_translate("Dialog", "오늘의 박스 오피스"))
        self.label_3.setText(_translate("Dialog", "누적 관객수"))
        self.label_4.setText(_translate("Dialog", "누적 매출액"))
        self.label_5.setText(_translate("Dialog", "상세정보"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "검색"))
        self.pushButton.setText(_translate("Dialog", "메일 보내기"))
        self.lineEdit_mail_PW.setPlaceholderText(_translate("Dialog", "PASSWORD"))
        self.lineEdit_mail_ID.setPlaceholderText(_translate("Dialog", "ID"))
        self.lineEdit_mail_address.setPlaceholderText(_translate("Dialog", "MAIL ADDRASS"))
        self.lineEdit_mail_address_2.setPlaceholderText(_translate("Dialog", "MAIL SUBJECT "))
        self.label.setText(_translate("Dialog", "메일 보내기"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "메일"))

