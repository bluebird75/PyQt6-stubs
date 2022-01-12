import typing
from PyQt6 import QtCore

some_bytearray = QtCore.QByteArray(3, b'a')
some_bytes = bytes(some_bytearray)	# type: bytes


