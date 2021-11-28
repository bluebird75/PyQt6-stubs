# The PEP 484 type hints stub file for the QtX11Extras module.
#
# Generated by SIP 6.0.3
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt5.
# 
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
# 
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
# 
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


import typing

from PyQt5 import sip
from PyQt5 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class Display(sip.simplewrapper): ...


class xcb_connection_t(sip.simplewrapper): ...


class QX11Info(sip.simplewrapper):

    def __init__(self, a0: 'QX11Info') -> None: ...

    @staticmethod
    def connection() -> xcb_connection_t: ...
    @staticmethod
    def display() -> Display: ...
    @staticmethod
    def setNextStartupId(id: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    @staticmethod
    def nextStartupId() -> QtCore.QByteArray: ...
    @staticmethod
    def getTimestamp() -> int: ...
    @staticmethod
    def setAppUserTime(time: int) -> None: ...
    @staticmethod
    def setAppTime(time: int) -> None: ...
    @staticmethod
    def appUserTime() -> int: ...
    @staticmethod
    def appTime() -> int: ...
    @staticmethod
    def appScreen() -> int: ...
    @staticmethod
    def appRootWindow(screen: int = ...) -> int: ...
    @staticmethod
    def appDpiY(screen: int = ...) -> int: ...
    @staticmethod
    def appDpiX(screen: int = ...) -> int: ...
    @staticmethod
    def isPlatformX11() -> bool: ...
