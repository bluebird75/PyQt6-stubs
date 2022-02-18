# The PEP 484 type hints stub file for the QtWebEngineWidgets module.
#
# Generated by SIP 6.2.0
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6-WebEngine.
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

from PyQt6 import QtGui
from PyQt6 import QtWebChannel
from PyQt6 import QtWidgets
from PyQt6 import QtWebEngineCore
from PyQt6 import QtPrintSupport
from PyQt6 import QtNetwork
from PyQt6 import QtCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QWebEngineView(QtWidgets.QWidget):

    def __init__(self, parent: typing.Optional[QtWidgets.QWidget] = ...) -> None: ...

    printFinished: typing.ClassVar[QtCore.pyqtSignal]
    printRequested: typing.ClassVar[QtCore.pyqtSignal]
    pdfPrintingFinished: typing.ClassVar[QtCore.pyqtSignal]
    def print(self, printer: QtPrintSupport.QPrinter) -> None: ...
    @typing.overload
    def printToPdf(self, filePath: str, pageLayout: QtGui.QPageLayout = ..., ranges: QtGui.QPageRanges = ...) -> None: ...
    @typing.overload
    def printToPdf(self, resultCallback: typing.Callable[[QtCore.QByteArray], None], pageLayout: QtGui.QPageLayout = ..., ranges: QtGui.QPageRanges = ...) -> None: ...
    def lastContextMenuRequest(self) -> QtWebEngineCore.QWebEngineContextMenuRequest: ...
    def createStandardContextMenu(self) -> QtWidgets.QMenu: ...
    def findText(self, subString: str, options: QtWebEngineCore.QWebEnginePage.FindFlag = ..., resultCallback: typing.Optional[typing.Callable[[bool], None]] = ...) -> None: ...
    @staticmethod
    def forPage(page: QtWebEngineCore.QWebEnginePage) -> 'QWebEngineView': ...
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None: ...
    def dropEvent(self, e: QtGui.QDropEvent) -> None: ...
    def dragMoveEvent(self, e: QtGui.QDragMoveEvent) -> None: ...
    def dragLeaveEvent(self, e: QtGui.QDragLeaveEvent) -> None: ...
    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None: ...
    def hideEvent(self, a0: QtGui.QHideEvent) -> None: ...
    def showEvent(self, a0: QtGui.QShowEvent) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def contextMenuEvent(self, a0: QtGui.QContextMenuEvent) -> None: ...
    def createWindow(self, type: QtWebEngineCore.QWebEnginePage.WebWindowType) -> 'QWebEngineView': ...
    renderProcessTerminated: typing.ClassVar[QtCore.pyqtSignal]
    iconChanged: typing.ClassVar[QtCore.pyqtSignal]
    iconUrlChanged: typing.ClassVar[QtCore.pyqtSignal]
    urlChanged: typing.ClassVar[QtCore.pyqtSignal]
    selectionChanged: typing.ClassVar[QtCore.pyqtSignal]
    titleChanged: typing.ClassVar[QtCore.pyqtSignal]
    loadFinished: typing.ClassVar[QtCore.pyqtSignal]
    loadProgress: typing.ClassVar[QtCore.pyqtSignal]
    loadStarted: typing.ClassVar[QtCore.pyqtSignal]
    def reload(self) -> None: ...
    def forward(self) -> None: ...
    def back(self) -> None: ...
    def stop(self) -> None: ...
    def icon(self) -> QtGui.QIcon: ...
    def settings(self) -> QtWebEngineCore.QWebEngineSettings: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def setZoomFactor(self, factor: float) -> None: ...
    def zoomFactor(self) -> float: ...
    def triggerPageAction(self, action: QtWebEngineCore.QWebEnginePage.WebAction, checked: bool = ...) -> None: ...
    def pageAction(self, action: QtWebEngineCore.QWebEnginePage.WebAction) -> QtGui.QAction: ...
    def selectedText(self) -> str: ...
    def hasSelection(self) -> bool: ...
    def iconUrl(self) -> QtCore.QUrl: ...
    def url(self) -> QtCore.QUrl: ...
    def setUrl(self, url: QtCore.QUrl) -> None: ...
    def title(self) -> str: ...
    def history(self) -> QtWebEngineCore.QWebEngineHistory: ...
    def setContent(self, data: QtCore.QByteArray, mimeType: str = ..., baseUrl: QtCore.QUrl = ...) -> None: ...
    def setHtml(self, html: str, baseUrl: QtCore.QUrl = ...) -> None: ...
    @typing.overload
    def load(self, url: QtCore.QUrl) -> None: ...
    @typing.overload
    def load(self, request: QtWebEngineCore.QWebEngineHttpRequest) -> None: ...
    def setPage(self, page: QtWebEngineCore.QWebEnginePage) -> None: ...
    def page(self) -> QtWebEngineCore.QWebEnginePage: ...
