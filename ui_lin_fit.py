# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line_fit_copy.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget  # add this line


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_load = QtWidgets.QPushButton(self.centralwidget)
        self.btn_load.setObjectName("btn_load")
        self.btn_load.setToolTip("load the data")
        self.gridLayout.addWidget(self.btn_load, 1, 0, 1, 1)
        self.btn_clean = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clean.setObjectName("btn_clean")
        self.btn_clean.setToolTip("clean the window and equation")
        self.gridLayout.addWidget(self.btn_clean, 1, 1, 1, 1)
        self.show_eq = QtWidgets.QLineEdit(self.centralwidget)
        self.show_eq.setObjectName("show_eq")
        self.show_eq.setToolTip("the equation of the fitting curve")
        self.gridLayout.addWidget(self.show_eq, 1, 4, 1, 1)
        self.label_eq = QtWidgets.QLabel(self.centralwidget)
        self.label_eq.setObjectName("label_eq")
        self.gridLayout.addWidget(self.label_eq, 1, 2, 1, 1)

        # class name = GraphicsLayoutWidget
        self.show_win = GraphicsLayoutWidget(self.centralwidget)
        self.show_win.setObjectName("show_win")
        self.show_win.setToolTip("the data and the fitting curve")
        self.gridLayout.addWidget(self.show_win, 0, 0, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Line Fitting"))
        self.btn_load.setText(_translate("MainWindow", "Load"))
        self.btn_clean.setText(_translate("MainWindow", "Clean"))
        self.label_eq.setText(_translate("MainWindow", "    Equation :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
