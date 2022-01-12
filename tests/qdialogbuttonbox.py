from PyQt6 import QtWidgets

a = QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel  # type: QtWidgets.QDialogButtonBox.StandardButton
b = a | QtWidgets.QDialogButtonBox.StandardButton.Ok  # type: QtWidgets.QDialogButtonBox.StandardButton
c = a | a  # type: QtWidgets.QDialogButtonBox.StandardButton
# not supported because StandardButton is a enum.Flag: d = a | 0
