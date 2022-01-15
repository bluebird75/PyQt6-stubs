from PyQt6.QtCore import pyqtSlot, QCoreApplication, QTimer, QObject, pyqtSignal

called = {}

class MyObj(QObject):
    sig_with_none = pyqtSignal([])
    sig_with_str  = pyqtSignal([str])
    sig_with_2str  = pyqtSignal([str, str])
    sig_with_int  = pyqtSignal([int])

    @pyqtSlot()
    def func_none(self) -> None:
        global called
        called['func_none'] = True
        return

    @pyqtSlot(int, result=int)
    def func_int(self, i: int) -> int:
        global called
        called['func_int'] = True
        return 42

    @pyqtSlot(str, result='QString')
    def func_str(self, s: str) -> str:
        global called
        called['func_str'] = True
        return '42'

    @pyqtSlot(str, str, name='my_name', revision=33, result='QString')
    def func_2str(self, s1: str, s2: str) -> None:
        global called
        called['func_2str'] = True


# app = QCoreApplication(['program', '-platform', 'offscreen'])

o = MyObj()
o.sig_with_none.connect(o.func_none)
o.sig_with_int.connect(o.func_int)
o.sig_with_str.connect(o.func_str)
o.sig_with_2str.connect(o.func_2str)

o.sig_with_none.emit()
o.sig_with_int.emit(33)
o.sig_with_str.emit('abc')
o.sig_with_2str.emit('abc', 'def')

n: None = o.func_none()
i: int = o.func_int(33)
s: str = o.func_str('abc')

# print(called)