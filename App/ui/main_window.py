# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1205, 675)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_all_workers_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_all_workers_btn.setObjectName("show_all_workers_btn")
        self.horizontalLayout.addWidget(self.show_all_workers_btn)
        self.show_local_workers_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_local_workers_btn.setObjectName("show_local_workers_btn")
        self.horizontalLayout.addWidget(self.show_local_workers_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.show_worker_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_worker_btn.setObjectName("show_worker_btn")
        self.verticalLayout.addWidget(self.show_worker_btn)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.add_worker_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_worker_btn.setObjectName("add_worker_btn")
        self.horizontalLayout_2.addWidget(self.add_worker_btn)
        self.delete_worker_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_worker_btn.setObjectName("delete_worker_btn")
        self.horizontalLayout_2.addWidget(self.delete_worker_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.show_all_preferences_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_all_preferences_btn.setObjectName("show_all_preferences_btn")
        self.horizontalLayout_3.addWidget(self.show_all_preferences_btn)
        self.show_local_preferences_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_local_preferences_btn.setObjectName("show_local_preferences_btn")
        self.horizontalLayout_3.addWidget(self.show_local_preferences_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.show_worker_preference_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_worker_preference_btn.setObjectName("show_worker_preference_btn")
        self.verticalLayout_2.addWidget(self.show_worker_preference_btn)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.delete_preference_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_preference_btn.setObjectName("delete_preference_btn")
        self.horizontalLayout_4.addWidget(self.delete_preference_btn)
        self.add_preference_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_preference_btn.setObjectName("add_preference_btn")
        self.horizontalLayout_4.addWidget(self.add_preference_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.show_insurances_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_insurances_btn.setObjectName("show_insurances_btn")
        self.verticalLayout_3.addWidget(self.show_insurances_btn)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.delete_insurance_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_insurance_btn.setObjectName("delete_insurance_btn")
        self.horizontalLayout_5.addWidget(self.delete_insurance_btn)
        self.add_insurance_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_insurance_btn.setObjectName("add_insurance_btn")
        self.horizontalLayout_5.addWidget(self.add_insurance_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.show_insurers_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_insurers_btn.setObjectName("show_insurers_btn")
        self.verticalLayout_6.addWidget(self.show_insurers_btn)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.add_insurer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_insurer_btn.setObjectName("add_insurer_btn")
        self.horizontalLayout_7.addWidget(self.add_insurer_btn)
        self.delete_insurer_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_insurer_btn.setObjectName("delete_insurer_btn")
        self.horizontalLayout_7.addWidget(self.delete_insurer_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.show_positions_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_positions_btn.setObjectName("show_positions_btn")
        self.verticalLayout_4.addWidget(self.show_positions_btn)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.add_position_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_position_btn.setObjectName("add_position_btn")
        self.horizontalLayout_6.addWidget(self.add_position_btn)
        self.delete_position_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_position_btn.setObjectName("delete_position_btn")
        self.horizontalLayout_6.addWidget(self.delete_position_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setObjectName("clear_btn")
        self.verticalLayout_5.addWidget(self.clear_btn)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1205, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "App"))
        self.show_all_workers_btn.setText(_translate("MainWindow", "Show all workers"))
        self.show_local_workers_btn.setText(_translate("MainWindow", "Show local workers"))
        self.show_worker_btn.setText(_translate("MainWindow", "Show worker"))
        self.add_worker_btn.setText(_translate("MainWindow", "Add worker"))
        self.delete_worker_btn.setText(_translate("MainWindow", "Delete worker"))
        self.show_all_preferences_btn.setText(_translate("MainWindow", "Show all preferences"))
        self.show_local_preferences_btn.setText(_translate("MainWindow", "Show local preferences"))
        self.show_worker_preference_btn.setText(_translate("MainWindow", "Show worker preference"))
        self.delete_preference_btn.setText(_translate("MainWindow", "Delete preference"))
        self.add_preference_btn.setText(_translate("MainWindow", "Add preference"))
        self.show_insurances_btn.setText(_translate("MainWindow", "Show insurances"))
        self.delete_insurance_btn.setText(_translate("MainWindow", "Delete insurance"))
        self.add_insurance_btn.setText(_translate("MainWindow", "Add insurance"))
        self.show_insurers_btn.setText(_translate("MainWindow", "Show insurers"))
        self.add_insurer_btn.setText(_translate("MainWindow", "Add insurer"))
        self.delete_insurer_btn.setText(_translate("MainWindow", "Delete insurer"))
        self.show_positions_btn.setText(_translate("MainWindow", "Show posiotions"))
        self.add_position_btn.setText(_translate("MainWindow", "Add position"))
        self.delete_position_btn.setText(_translate("MainWindow", "Delete position"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
