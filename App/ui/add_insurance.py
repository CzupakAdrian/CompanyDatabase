# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_position.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(226, 133)

        self.formBox = QtWidgets.QGroupBox("formBox")
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")

        self.id = QtWidgets.QLineEdit(Dialog)
        self.id.setObjectName("insurance id")
        self.formLayout.addRow(QtWidgets.QLabel("insurance id"), self.id)

        self.insurer = QtWidgets.QLineEdit(Dialog)
        self.insurer.setObjectName("insurer")
        self.formLayout.addRow(QtWidgets.QLabel("insurer id"), self.insurer)

        self.date = QtWidgets.QDateEdit(Dialog)
        self.date.setObjectName("expiration_date")
        self.formLayout.addRow(QtWidgets.QLabel("expiration date"), self.date)

        self.formBox.setLayout(self.formLayout)

        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        mainLayout = QtWidgets.QVBoxLayout()
        mainLayout.addWidget(self.formBox)
        mainLayout.addWidget(self.buttonBox)
        Dialog.setLayout(mainLayout)

        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Add insurance"))


