# The PEP 484 type hints stub file for the QtMultimediaWidgets module.
#
# Generated by SIP 6.5.0
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6.
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


import enum
import typing


import PyQt6.sip

from PyQt6 import QtWidgets
from PyQt6 import QtMultimedia
from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

class QGraphicsVideoItem(QtWidgets.QGraphicsObject):

    def __init__(self, parent: typing.Optional[QtWidgets.QGraphicsItem] = ...) -> None: ...

    def itemChange(self, change: QtWidgets.QGraphicsItem.GraphicsItemChange, value: typing.Any) -> typing.Any: ...
    def timerEvent(self, event: QtCore.QTimerEvent) -> None: ...
    nativeSizeChanged: typing.ClassVar[QtCore.pyqtSignal]
    def type(self) -> int: ...
    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionGraphicsItem, widget: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...
    def boundingRect(self) -> QtCore.QRectF: ...
    def nativeSize(self) -> QtCore.QSizeF: ...
    def setSize(self, size: QtCore.QSizeF) -> None: ...
    def size(self) -> QtCore.QSizeF: ...
    def setOffset(self, offset: QtCore.QPointF) -> None: ...
    def offset(self) -> QtCore.QPointF: ...
    def setAspectRatioMode(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    def aspectRatioMode(self) -> QtCore.Qt.AspectRatioMode: ...
    def videoSink(self) -> QtMultimedia.QVideoSink: ...


class QVideoWidget(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    def moveEvent(self, event: QtGui.QMoveEvent) -> None: ...
    def resizeEvent(self, event: QtGui.QResizeEvent) -> None: ...
    def hideEvent(self, event: QtGui.QHideEvent) -> None: ...
    def showEvent(self, event: QtGui.QShowEvent) -> None: ...
    def event(self, event: QtCore.QEvent) -> bool: ...
    def aspectRatioModeChanged(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    fullScreenChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setAspectRatioMode(self, mode: QtCore.Qt.AspectRatioMode) -> None: ...
    def setFullScreen(self, fullScreen: bool) -> None: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def isFullScreen(self) -> bool: ...
    def aspectRatioMode(self) -> QtCore.Qt.AspectRatioMode: ...
    def videoSink(self) -> QtMultimedia.QVideoSink: ...
