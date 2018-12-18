import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_lin_fit import Ui_MainWindow
import pyqtgraph as pg
import numpy as np
from scipy import optimize
from pyexcel_ods import get_data


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        # setting of figure. NOTE: this needs to be above self.setupUi(self)
        pg.setConfigOption('background', '#f0f0f0')
        pg.setConfigOption('foreground', 'd')
        pg.setConfigOptions(antialias=True)

        self.setupUi(self)
        self.btn_clean.clicked.connect(self.clean_all)
        # self.btn_load.clicked.connect(self.getfile)
        self.btn_load.clicked.connect(self.getequ)  # testing function
        self.show_eq.setReadOnly(True)

    def getequ(self):
        str = self.fit_eq.toPlainText().split("\n")
        args = str[0].replace(" ", "").split(',')

        func_args = ""
        for arg in args
            func_args = "fit_func = lambda x"
        # to_be_exec = "global to_fit_equ;" + "to_fit_equ=" + equ_str
        # exec(to_be_exec)

    @pyqtSlot()
    def getfile(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open file', './', "(*.csv *.ods *.xlsm *.xlsx)")
        if file_path:
            data_read = get_data(file_path)
            try:
                x_data = list(data_read.values())[0][0]
                y_data = list(data_read.values())[0][1]
                self.renew(x_data, y_data)
            except ValueError:
                QMessageBox.information(self, "ValueError", "Some elements in data are not float.")
            except RuntimeError:
                QMessageBox.information(self, "RuntimeError", "The least-squares minimization fails")

    # plot the data and fitting curve to the window
    def renew(self, x_data, y_data):  # x_data and y_data must be lists
        x_data = np.asarray(x_data)
        y_data = np.asarray(y_data)

        self.clean_all()
        plt = self.show_win.addPlot()  # ready to plot
        plt.plot(x_data, y_data, pen=None, symbol='o')

        def fit_func(x, a, b):  # define optimize function
            return a * x + b

        params, params_covariance = optimize.curve_fit(fit_func, x_data, y_data)
        a_fit = params[0]
        b_fit = params[1]
        plt.plot(x_data, fit_func(x_data, a_fit, b_fit),
                 pen=pg.mkPen(color='#333', width=2))
        equ = "y = " + "%.3e" % (a_fit) + " x + " + "%.3e" % (b_fit)

        # standard deviation errors, first one is for x, second one is for y
        SDEs = np.sqrt(np.diag(params_covariance))
        x_sd = SDEs[0]
        y_sd = SDEs[1]
        self.show_eq.setText(equ + "\n" + "standard deviation of x: " + "%.3e" % (x_sd) +
                             "\n" + "standard deviation of y: " + "%.3e" % (y_sd))

    @pyqtSlot()
    def clean_all(self):
        self.show_win.clear()
        self.show_eq.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
