# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 192)
        self.path_edit = QtWidgets.QTextEdit(Form)
        self.path_edit.setGeometry(QtCore.QRect(11, 55, 501, 51))
        self.path_edit.setObjectName("path_edit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 140, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(11, 11, 405, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(11, 33, 295, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.on_click_button)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "cat or dog"))
        self.label.setText(_translate("Form", "鼠标拖拽图片至下方编辑框点击按钮即可预测图片是猫还是狗"))
        self.label_2.setText(_translate("Form", "自信度为[0,1]之间，越大代表对结果越肯定"))

