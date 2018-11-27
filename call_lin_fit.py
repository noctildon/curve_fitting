import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_lin_fit import Ui_MainWindow  # import UI
import pyqtgraph as pg
import numpy as np
from scipy import optimize
from pyexcel_ods import get_data


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        # figure option setting. NOTE: this needs to be above self.setupUi(self)
        pg.setConfigOption('background', '#f0f0f0')  # set background color
        pg.setConfigOption('foreground', 'd')        # set foreground color
        pg.setConfigOptions(antialias=True)          # make the graph smooth

        self.setupUi(self)
        self.btn_clean.clicked.connect(self.clean_all)
        self.btn_load.clicked.connect(self.getfile)
        self.show_eq.setReadOnly(True)  # set show_eq to be read only

    @pyqtSlot()
    def getfile(self):
        # filter file and get the file path
        file_path, _ = QFileDialog.getOpenFileName(
            self, 'Open file', './', "(*.csv *.ods *.xlsm *.xlsx)")
        if file_path:  # check if the file is loaded
            data_read = get_data(file_path)
            try:
                x_data = list(data_read.values())[0][0]  # first line of data
                y_data = list(data_read.values())[0][1]  # second line of data
                self.renew(x_data, y_data)
            except ValueError:
                QMessageBox.information(self, "ValueError", "Some elements in data are not float.")
            except RuntimeError:
                QMessageBox.information(self, "RuntimeError", "The least-squares minimization fails")

    # plot the data and fitting curve to the window
    def renew(self, x_data, y_data):  # x_data and y_data must be lists
        # change the list to numpy list
        x_data = np.asarray(x_data)
        y_data = np.asarray(y_data)

        self.clean_all()  # clean the window and the equation
        plt = self.show_win.addPlot()  # ready to plot
        # plot the raw data point
        plt.plot(x_data, y_data, pen=None, symbol='o')

        def fit_func(x, a, b):  # define optimize function
            return a * x + b

        params, params_covariance = optimize.curve_fit(fit_func, x_data, y_data)  # fit the raw data
        a_fit = params[0]  # fitting curve a parameter
        b_fit = params[1]  # fitting curve b parameter
        plt.plot(x_data, fit_func(x_data, a_fit, b_fit),
                 pen=pg.mkPen(color='#333', width=2))  # plot the fitting curve
        equ = "y = " + "%.3e" % (a_fit) + " x + " + "%.3e" % (b_fit)

        # standard deviation errors, first one is for x, second one is for y
        SDEs = np.sqrt(np.diag(params_covariance))
        x_sd = SDEs[0]  # standard deviation errors of x
        y_sd = SDEs[1]  # standard deviation errors of y
        # show the fitting curve equation
        self.show_eq.setText(equ + "\n" + "standard deviation of x: " + "%.3e" % (x_sd) +
                             "\n" + "standard deviation of y: " + "%.3e" % (y_sd))

    @pyqtSlot()
    def clean_all(self):
        self.show_win.clear()     # clean the window
        self.show_eq.setText("")  # clean the equation


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
