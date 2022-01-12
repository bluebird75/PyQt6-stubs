from PyQt6 import QtWidgets

a = QtWidgets.QMessageBox.StandardButton.Ok # type: QtWidgets.QMessageBox.StandardButton
a_int = QtWidgets.QMessageBox.StandardButton.Ok # type: int

b = a | 1 # type: QtWidgets.QMessageBox.StandardButton
b_int = a_int | 1 # type: int

c = QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel  # type: QtWidgets.QMessageBox.StandardButton
c_int = QtWidgets.QMessageBox.StandardButton.Ok | QtWidgets.QMessageBox.StandardButton.Cancel  # type: int

d = a | c  # type: QtWidgets.QMessageBox.StandardButton
d_int = a_int | c_int # type: int