import typing

from PyQt6.QtCore import QObject, QProcess, QCoreApplication
from PyQt6.QtWidgets import QWidget, QApplication


app = QCoreApplication([])

o1 = QProcess()
o2 = QObject(parent=o1)
o3 = QProcess(parent=o1)

a = o1.findChildren(QObject)  # type: typing.List[QObject]
b = o1.findChildren(QProcess)  # type: typing.List[QProcess]
c = o1.findChildren((QObject,))  # type: typing.List[QObject]
d = o1.findChildren((QProcess,))  # type: typing.List[QProcess]
e = o1.findChildren((QProcess, QObject))  # type: typing.List[QObject]

f = o1.findChild(QObject)   # type: QObject
g = o1.findChild(QProcess)   # type: QProcess
h = o1.findChild((QProcess, QObject))   # type: QObject

assert type(a) == list
assert isinstance(a[0], QObject)
assert isinstance(a[1], QObject)

assert type(b) == list
assert isinstance(b[0], QProcess)

assert type(c) == list
assert isinstance(c[0], QObject)
assert isinstance(c[1], QObject)

assert type(d) == list
assert isinstance(d[0], QProcess)

assert type(e) == list
assert isinstance(e[0], QObject)
assert isinstance(e[1], QObject)

assert isinstance(f, QObject)
assert isinstance(g, QProcess)
assert isinstance(h, QObject)
