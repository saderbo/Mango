# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ObjectTest2.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(376, 299)
        self.textInput = QtWidgets.QTextEdit(Form)
        self.textInput.setGeometry(QtCore.QRect(20, 210, 331, 31))
        self.textInput.setObjectName("textInput")
        self.textList = QtWidgets.QTextBrowser(Form)
        self.textList.setGeometry(QtCore.QRect(20, 10, 331, 192))
        self.textList.setObjectName("textList")
        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setGeometry(QtCore.QRect(270, 260, 75, 23))
        self.btnSave.setObjectName("btnSave")
        self.btnClose = QtWidgets.QPushButton(Form)
        self.btnClose.setGeometry(QtCore.QRect(20, 260, 75, 23))
        self.btnClose.setObjectName("btnClose")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "디자인 구려요"))
        self.btnSave.setText(_translate("Form", "등록"))
        self.btnClose.setText(_translate("Form", "종료"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

