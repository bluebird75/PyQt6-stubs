import typing

from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget, QApplication


app = QApplication(['program', '-platform', 'offscreen'])

o1 = QWidget()
o2 = QObject(parent=o1)
o3 = QWidget(parent=o1)

a = o1.findChildren(QObject)  # type: typing.List[QObject]
b = o1.findChildren(QWidget)  # type: typing.List[QWidget]
c = o1.findChildren((QObject,))  # type: typing.List[QObject]
d = o1.findChildren((QWidget,))  # type: typing.List[QWidget]
e = o1.findChildren((QWidget, QObject))  # type: typing.List[QObject]

f = o1.findChild(QObject)   # type: QObject
g = o1.findChild(QWidget)   # type: QWidget
h = o1.findChild((QWidget, QObject))   # type: QObject

assert type(a) == list
assert isinstance(a[0], QObject)
assert isinstance(a[1], QObject)

assert type(b) == list
assert isinstance(b[0], QWidget)

assert type(c) == list
assert isinstance(c[0], QObject)
assert isinstance(c[1], QObject)

assert type(d) == list
assert isinstance(d[0], QWidget)

assert type(e) == list
assert isinstance(e[0], QObject)
assert isinstance(e[1], QObject)

assert isinstance(f, QObject)
assert isinstance(g, QWidget)
assert isinstance(h, QObject)
