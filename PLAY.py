# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PLAY.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 400)
        self.restart = QtWidgets.QPushButton(Form)
        self.restart.setGeometry(QtCore.QRect(490, 350, 75, 23))
        self.restart.setObjectName("restart")
        self.return_2 = QtWidgets.QPushButton(Form)
        self.return_2.setGeometry(QtCore.QRect(570, 350, 75, 23))
        self.return_2.setObjectName("return_2")
        self.enter = QtWidgets.QPushButton(Form)
        self.enter.setGeometry(QtCore.QRect(400, 320, 75, 23))
        self.enter.setObjectName("enter")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 320, 181, 31))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 20, 361, 281))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.restart.setText(_translate("Form", "重新開始"))
        self.return_2.setText(_translate("Form", "返回"))
        self.enter.setText(_translate("Form", "輸入"))
