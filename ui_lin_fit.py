# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lin_fit.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget  # @


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(875, 662)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_win = GraphicsLayoutWidget(self.centralwidget)  # @
        self.show_win.setGeometry(QtCore.QRect(10, 10, 851, 431))
        self.show_win.setObjectName("show_win")
        self.show_win.setToolTip("the data and the fitting curve")  # @
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(15, 447, 851, 201))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.dashboard = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.dashboard.setObjectName("dashboard")
        self.fit_equation = QtWidgets.QHBoxLayout()
        self.fit_equation.setObjectName("fit_equation")
        self.fit_eq_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fit_eq_label.setObjectName("fit_eq_label")
        self.fit_equation.addWidget(self.fit_eq_label)
        self.fit_eq = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.fit_eq.setObjectName("fit_eq")
        self.fit_eq.setToolTip('The equation to be fitted')
        self.fit_equation.addWidget(self.fit_eq)
        self.dashboard.addLayout(self.fit_equation)
        self.btns_windows = QtWidgets.QHBoxLayout()
        self.btns_windows.setObjectName("btns_windows")
        self.btns = QtWidgets.QVBoxLayout()
        self.btns.setObjectName("btns")
        self.btn_load = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_load.setObjectName("btn_load")
        self.btn_load.setToolTip("load the data")  # @
        self.btns.addWidget(self.btn_load)
        self.btn_clean = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_clean.setObjectName("btn_clean")
        self.btn_clean.setToolTip("clean the window and equation")  # @
        self.btns.addWidget(self.btn_clean)
        self.btns_windows.addLayout(self.btns)
        self.show_eq = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.show_eq.setObjectName("show_eq")
        self.show_eq.setToolTip("the equation of the fitting curve")  # @
        self.btns_windows.addWidget(self.show_eq)
        self.dashboard.addLayout(self.btns_windows)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Line Fitting"))
        self.fit_eq_label.setText(_translate("MainWindow", " Fit equation"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.btn_clean.setText(_translate("MainWindow", "Clean"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
