# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\lab_01\installer\installer_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Installer(object):
    def setupUi(self, Installer):
        Installer.setObjectName("Installer")
        Installer.resize(627, 300)
        self.nextBtn = QtWidgets.QPushButton(Installer)
        self.nextBtn.setGeometry(QtCore.QRect(150, 180, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nextBtn.setFont(font)
        self.nextBtn.setObjectName("nextBtn")
        self.label = QtWidgets.QLabel(Installer)
        self.label.setGeometry(QtCore.QRect(50, 40, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.cancelBtn = QtWidgets.QPushButton(Installer)
        self.cancelBtn.setGeometry(QtCore.QRect(360, 180, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancelBtn.setFont(font)
        self.cancelBtn.setObjectName("cancelBtn")

        self.retranslateUi(Installer)
        QtCore.QMetaObject.connectSlotsByName(Installer)

    def retranslateUi(self, Installer):
        _translate = QtCore.QCoreApplication.translate
        Installer.setWindowTitle(_translate("Installer", "Dialog"))
        self.nextBtn.setText(_translate("Installer", "Далее"))
        self.label.setText(_translate("Installer", "Приветствуем в установщике замечательной программы.\n"
"Для установки нажмите \"Далее\", для отмены \"Выход\""))
        self.cancelBtn.setText(_translate("Installer", "Выход"))
