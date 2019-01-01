import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_lin_fit import Ui_MainWindow
import pyqtgraph as pg
from numpy import *
from scipy import optimize
from pyexcel_ods import get_data
import pyexcel_io.readers
import pyexcel_io.writers
import pyexcel_io.database
import pyexcel_io.readers.csvr


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)

        # setting of figure. NOTE: this needs to be above self.setupUi(self)
        pg.setConfigOption('background', '#f0f0f0')
        pg.setConfigOption('foreground', 'd')
        pg.setConfigOptions(antialias=True)

        self.setupUi(self)
        self.btn_clean.clicked.connect(self.clean_all)
        self.btn_load.clicked.connect(self.getfile)
        # self.btn_load.clicked.connect(self.getfunc)
        self.show_eq.setReadOnly(True)

    def getfunc(self):
        # first line is arguments, second line is the function to be fitted
        str = self.fit_eq.toPlainText().split("\n")
        args = str[0].replace(" ", "").split(',')
        to_be_exec = "fit_func = lambda x"
        for arg in args:
            to_be_exec += ", " + arg
        to_be_exec += ":" + str[1]
        exec("global fit_func;" + to_be_exec)
        return args

    @pyqtSlot()
    def getfile(self):
        if self.fit_eq.toPlainText() == "":
            QMessageBox.information(self, "Empty value", "Empty equation format\nInsert the function to be fitted")
        else:
            self.getfunc()
            file_path, _ = QFileDialog.getOpenFileName(
                self, 'Open file', './', "(*.csv *.ods *.xlsm *.xlsx)")
            if file_path:
                data_read = get_data(file_path)
                try:
                    x_data = list(data_read.values())[0][0]
                    y_data = list(data_read.values())[0][1]
                    self.renew(fit_func, x_data, y_data)
                except ValueError:
                    QMessageBox.information(self, "Value Error", "Some elements in data are not float.")
                except RuntimeError:
                    QMessageBox.information(self, "Runtime Error", "The least-squares minimization fails")

    # plot the data and fitting curve to the window
    def renew(self, fit_func, x_data, y_data):  # x_data and y_data must be lists
        def wrapper(func, args):
            return func(*args)

        self.clean_all()
        plt = self.show_win.addPlot()  # ready to plot
        plt.plot(x_data, y_data, pen=None, symbol='o')

        params, params_covariance = optimize.curve_fit(fit_func, x_data, y_data)
        params = params.tolist()

        fit_y_data = []
        for x in x_data:
            fit_y_data.append(wrapper(fit_func, [x] + params))

        plt.plot(x_data, fit_y_data, pen=pg.mkPen(color='#333', width=2))

        args = self.getfunc()
        SDEs = sqrt(diag(params_covariance))  # standard deviation errors
        show_text = ''
        for id, arg in enumerate(args):
            show_text += '{} = {:.2e} ± {:.2e} \n'.format(arg, params[id], SDEs[id])
        self.show_eq.setText(show_text)

    @pyqtSlot()
    def clean_all(self):
        self.show_win.clear()
        self.show_eq.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
