import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_lin_fit import Ui_MainWindow  # import UI
import pyqtgraph as pg  # import plotting module
import numpy as np  # import computing module
from scipy import optimize
from pyexcel_ods import get_data
# official document of optimize : https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html
# TODO: add the running symbol showing that the application is running
# TODO: consider there are some titles in data file
# TODO: calculate the standard deviation
# TODO: add the feature of changing graph propeties(ex. color, width)
# TODO: test some wrong data(ex. empty value or non-number value), i.e., try errors
# TODO: format the output of the parameters


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
            # file_format = re.search('\.[A-Za-z]+$', file_path).group()  # get file format
            data_read = get_data(file_path)
            x_data = list(data_read.values())[0][0]  # first line of data
            y_data = list(data_read.values())[0][1]  # second line of data
            self.renew(x_data, y_data)

    # plot the data and fitting curve to the window
    def renew(self, x_data, y_data):  # x_data and y_data must be lists
        # change the list to numpy list
        x_data = np.asarray(x_data)
        y_data = np.asarray(y_data)

        self.clean_all()  # clean the window and the equation
        plt = self.show_win.addPlot()                   # ready to plot
        plt.plot(x_data, y_data, pen=None, symbol='o')  # plot the raw data point

        def fit_func(x, a, b):  # define optimize function
            return a * x + b

        params, params_covariance = optimize.curve_fit(fit_func, x_data, y_data)  # fit the raw data
        plt.plot(x_data, fit_func(x_data, params[0], params[1]),
                 pen=pg.mkPen(color='#333', width=2))  # plot the fitting curve
        self.show_eq.setText("y = " + str(params[0]) + "x + " + str(params[1]))  # show the fitting curve equation
        perr = np.sqrt(np.diag(params_covariance))  # standard deviation errors

    @pyqtSlot()
    def clean_all(self):
        self.show_win.clear()     # clean the window
        self.show_eq.setText("")  # clean the equation


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
