# Content

- [Content](#content)
- [Description](#description)
- [Prerequisites(for development)](#prerequisitesfor-development)
    - [Python modules](#python-modules)
- [Testing data](#testing-data)
- [Compatibility](#compatibility)
- [To do list](#to-do-list)


# Description

This gui application allows to linear fit the two dimensional data(in csv, ods, xlsm or xlsx).
It can show the data as well as the fitting curve in the same window.
The program can output the plotting and save it.
It also can show the equation of the fitting curve.
The central idea of this program is to utilize function **optimize** in Python module **SciPy**.
For more information about the usage of **optimize** and **SciPy**, check [link](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html)


# Prerequisites(for development)

## Python modules

The necessary Python modules contain
- PyQt5
- numpy
- openpyxl
- pyexcel
- pyexcel-io
- pyexcel-ods
- pyexcel-xls
- pyexcel-xlsx
- pyqtgraph
- scipy


To install the above Python modules(except PyQt5), one can run
```console
$ pip install -r requirements.txt
```


For the installation of PyQt5 specifically, check [link](https://github.com/noctildon/linux-tutorial#install-pyqt5-in-virtualenv)


# Testing data

One can use **test_data** to test the function of this program.


# Compatibility

The original Python code is only tested in Linux Mint 18.3.
But it should work in any OS installed required Python modules.


# To do list

- [ ] freeze the program to into stand-alone executables, also tested on Windows, Linux and MacOS.
- [ ] do "**TODO**" in call_lin_fit.py
- [ ] add demo gif