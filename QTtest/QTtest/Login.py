# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(361, 185)
        Login.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Login.setStyleSheet("selection-background-color: rgb(0, 0, 255);\n"
"selection-background-color: rgb(0, 0, 127);")
        self.layoutWidget = QtWidgets.QWidget(Login)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 162))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lab_nickname = QtWidgets.QLabel(self.layoutWidget)
        self.lab_nickname.setObjectName("lab_nickname")
        self.horizontalLayout_4.addWidget(self.lab_nickname)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.line_nickname = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_nickname.setObjectName("line_nickname")
        self.horizontalLayout_4.addWidget(self.line_nickname)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.lab_password = QtWidgets.QLabel(self.layoutWidget)
        self.lab_password.setObjectName("lab_password")
        self.horizontalLayout_5.addWidget(self.lab_password)
        spacerItem3 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.line_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_password.setObjectName("line_password")
        self.horizontalLayout_5.addWidget(self.line_password)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.but_setting = QtWidgets.QPushButton(self.layoutWidget)
        self.but_setting.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_setting.setObjectName("but_setting")
        self.horizontalLayout_6.addWidget(self.but_setting)
        self.but_login = QtWidgets.QPushButton(self.layoutWidget)
        self.but_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_login.setObjectName("but_login")
        self.horizontalLayout_6.addWidget(self.but_login)
        self.but_register = QtWidgets.QPushButton(self.layoutWidget)
        self.but_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_register.setObjectName("but_register")
        self.horizontalLayout_6.addWidget(self.but_register)
        self.but_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.but_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.but_cancel.setObjectName("but_cancel")
        self.horizontalLayout_6.addWidget(self.but_cancel)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.b = QtWidgets.QListWidget(Login)
        self.b.setGeometry(QtCore.QRect(-5, -9, 371, 201))
        self.b.setStyleSheet("border-image: url(:/images/background.png);")
        self.b.setObjectName("b")
        self.b.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(Login)
        self.but_cancel.clicked.connect(Login.close)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.lab_nickname.setText(_translate("Login", "Nickname"))
        self.lab_password.setText(_translate("Login", "Password"))
        self.but_setting.setText(_translate("Login", "Setting"))
        self.but_login.setText(_translate("Login", "Login"))
        self.but_register.setText(_translate("Login", "Register"))
        self.but_cancel.setText(_translate("Login", "Cancel"))

import resource
