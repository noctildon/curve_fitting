# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'line_fit.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import GraphicsLayoutWidget  # @


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(786, 551)  # @
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.show_win = GraphicsLayoutWidget(self.centralwidget)  # @
        self.show_win.setGeometry(QtCore.QRect(10, 10, 771, 421))
        self.show_win.setObjectName("show_win")
        self.show_win.setToolTip("the data and the fitting curve")  # @
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 443, 771, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.ctrl_window = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.ctrl_window.setObjectName("ctrl_window")
        self.btns = QtWidgets.QVBoxLayout()
        self.btns.setObjectName("btns")
        self.btn_load = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_load.setObjectName("btn_load")
        self.btn_load.setToolTip("load the data")  # @
        self.btns.addWidget(self.btn_load)
        self.btn_clean = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_clean.setObjectName("btn_clean")
        self.btn_clean.setToolTip("clean the window and equation")  # @
        self.btns.addWidget(self.btn_clean)
        self.ctrl_window.addLayout(self.btns)
        self.show_eq = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.show_eq.setToolTip("the equation of the fitting curve")  # @
        self.show_eq.setObjectName("show_eq")
        self.ctrl_window.addWidget(self.show_eq)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Line Fitting"))
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
