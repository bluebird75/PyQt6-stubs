# The PEP 484 type hints stub file for the Qt3DInput module.
#
# Generated by SIP 6.0.2
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt3D.
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
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import Qt3DCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class QAbstractActionInput(Qt3DCore.QNode): ...

class QAbstractAxisInput(Qt3DCore.QNode):

    def sourceDeviceChanged(self, sourceDevice: 'QAbstractPhysicalDevice') -> None: ...
    def setSourceDevice(self, sourceDevice: 'QAbstractPhysicalDevice') -> None: ...
    def sourceDevice(self) -> 'QAbstractPhysicalDevice': ...

class QAbstractPhysicalDevice(Qt3DCore.QNode):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def axisSettings(self) -> typing.List['QAxisSetting']: ...
    def removeAxisSetting(self, axisSetting: 'QAxisSetting') -> None: ...
    def addAxisSetting(self, axisSetting: 'QAxisSetting') -> None: ...
    def buttonIdentifier(self, name: str) -> int: ...
    def axisIdentifier(self, name: str) -> int: ...
    def buttonNames(self) -> typing.List[str]: ...
    def axisNames(self) -> typing.List[str]: ...
    def buttonCount(self) -> int: ...
    def axisCount(self) -> int: ...

class QAction(Qt3DCore.QNode):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def sceneChangeEvent(self, change: Qt3DCore.QSceneChange) -> None: ...
    def activeChanged(self, isActive: bool) -> None: ...
    def inputs(self) -> typing.List['QAbstractActionInput']: ...
    def removeInput(self, input: 'QAbstractActionInput') -> None: ...
    def addInput(self, input: 'QAbstractActionInput') -> None: ...
    def isActive(self) -> bool: ...

class QActionInput('QAbstractActionInput'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def buttonsChanged(self, buttons: typing.Iterable[int]) -> None: ...
    def sourceDeviceChanged(self, sourceDevice: 'QAbstractPhysicalDevice') -> None: ...
    def setButtons(self, buttons: typing.Iterable[int]) -> None: ...
    def setSourceDevice(self, sourceDevice: 'QAbstractPhysicalDevice') -> None: ...
    def buttons(self) -> typing.List[int]: ...
    def sourceDevice(self) -> 'QAbstractPhysicalDevice': ...

class QAnalogAxisInput('QAbstractAxisInput'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def axisChanged(self, axis: int) -> None: ...
    def setAxis(self, axis: int) -> None: ...
    def axis(self) -> int: ...

class QAxis(Qt3DCore.QNode):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def sceneChangeEvent(self, change: Qt3DCore.QSceneChange) -> None: ...
    def valueChanged(self, value: float) -> None: ...
    def value(self) -> float: ...
    def inputs(self) -> typing.List['QAbstractAxisInput']: ...
    def removeInput(self, input: 'QAbstractAxisInput') -> None: ...
    def addInput(self, input: 'QAbstractAxisInput') -> None: ...

class QAxisAccumulator(Qt3DCore.QComponent):

    class SourceAxisType(int):
        Velocity = ... # type: QAxisAccumulator.SourceAxisType
        Acceleration = ... # type: QAxisAccumulator.SourceAxisType

    Velocity = ...  # type: QAxisAccumulator.SourceAxisType
    Acceleration = ...  # type: QAxisAccumulator.SourceAxisType

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def sceneChangeEvent(self, change: Qt3DCore.QSceneChange) -> None: ...
    def scaleChanged(self, scale: float) -> None: ...
    def velocityChanged(self, value: float) -> None: ...
    def valueChanged(self, value: float) -> None: ...
    def sourceAxisTypeChanged(self, sourceAxisType: 'QAxisAccumulator.SourceAxisType') -> None: ...
    def sourceAxisChanged(self, sourceAxis: 'QAxis') -> None: ...
    def setScale(self, scale: float) -> None: ...
    def setSourceAxisType(self, sourceAxisType: 'QAxisAccumulator.SourceAxisType') -> None: ...
    def setSourceAxis(self, sourceAxis: 'QAxis') -> None: ...
    def scale(self) -> float: ...
    def velocity(self) -> float: ...
    def value(self) -> float: ...
    def sourceAxisType(self) -> 'QAxisAccumulator.SourceAxisType': ...
    def sourceAxis(self) -> 'QAxis': ...

class QAxisSetting(Qt3DCore.QNode):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def smoothChanged(self, smooth: bool) -> None: ...
    def axesChanged(self, axes: typing.Iterable[int]) -> None: ...
    def deadZoneRadiusChanged(self, deadZoneRadius: float) -> None: ...
    def setSmoothEnabled(self, enabled: bool) -> None: ...
    def setAxes(self, axes: typing.Iterable[int]) -> None: ...
    def setDeadZoneRadius(self, deadZoneRadius: float) -> None: ...
    def isSmoothEnabled(self) -> bool: ...
    def axes(self) -> typing.List[int]: ...
    def deadZoneRadius(self) -> float: ...

class QButtonAxisInput('QAbstractAxisInput'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def decelerationChanged(self, deceleration: float) -> None: ...
    def accelerationChanged(self, acceleration: float) -> None: ...
    def buttonsChanged(self, buttons: typing.Iterable[int]) -> None: ...
    def scaleChanged(self, scale: float) -> None: ...
    def setDeceleration(self, deceleration: float) -> None: ...
    def setAcceleration(self, acceleration: float) -> None: ...
    def setButtons(self, buttons: typing.Iterable[int]) -> None: ...
    def setScale(self, scale: float) -> None: ...
    def deceleration(self) -> float: ...
    def acceleration(self) -> float: ...
    def buttons(self) -> typing.List[int]: ...
    def scale(self) -> float: ...

class QInputAspect(Qt3DCore.QAbstractAspect):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def availablePhysicalDevices(self) -> typing.List[str]: ...
    def createPhysicalDevice(self, name: str) -> 'QAbstractPhysicalDevice': ...

class QInputChord('QAbstractActionInput'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def timeoutChanged(self, timeout: int) -> None: ...
    def setTimeout(self, timeout: int) -> None: ...
    def chords(self) -> typing.List['QAbstractActionInput']: ...
    def removeChord(self, input: 'QAbstractActionInput') -> None: ...
    def addChord(self, input: 'QAbstractActionInput') -> None: ...
    def timeout(self) -> int: ...

class QInputSequence('QAbstractActionInput'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def buttonIntervalChanged(self, buttonInterval: int) -> None: ...
    def timeoutChanged(self, timeout: int) -> None: ...
    def setButtonInterval(self, buttonInterval: int) -> None: ...
    def setTimeout(self, timeout: int) -> None: ...
    def sequences(self) -> typing.List['QAbstractActionInput']: ...
    def removeSequence(self, input: 'QAbstractActionInput') -> None: ...
    def addSequence(self, input: 'QAbstractActionInput') -> None: ...
    def buttonInterval(self) -> int: ...
    def timeout(self) -> int: ...

class QInputSettings(Qt3DCore.QComponent):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def eventSourceChanged(self, a0: QtCore.QObject) -> None: ...
    def setEventSource(self, eventSource: QtCore.QObject) -> None: ...
    def eventSource(self) -> QtCore.QObject: ...

class QKeyboardDevice('QAbstractPhysicalDevice'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def activeInputChanged(self, activeInput: 'QKeyboardHandler') -> None: ...
    def sceneChangeEvent(self, change: Qt3DCore.QSceneChange) -> None: ...
    def buttonIdentifier(self, name: str) -> int: ...
    def axisIdentifier(self, name: str) -> int: ...
    def buttonNames(self) -> typing.List[str]: ...
    def axisNames(self) -> typing.List[str]: ...
    def buttonCount(self) -> int: ...
    def axisCount(self) -> int: ...
    def activeInput(self) -> 'QKeyboardHandler': ...

class QKeyboardHandler(Qt3DCore.QComponent):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def sceneChangeEvent(self, change: Qt3DCore.QSceneChange) -> None: ...
    def released(self, event: 'QKeyEvent') -> None: ...
    def pressed(self, event: 'QKeyEvent') -> None: ...
    def volumeDownPressed(self, event: 'QKeyEvent') -> None: ...
    def volumeUpPressed(self, event: 'QKeyEvent') -> None: ...
    def menuPressed(self, event: 'QKeyEvent') -> None: ...
    def flipPressed(self, event: 'QKeyEvent') -> None: ...
    def hangupPressed(self, event: 'QKeyEvent') -> None: ...
    def callPressed(self, event: 'QKeyEvent') -> None: ...
    def context4Pressed(self, event: 'QKeyEvent') -> None: ...
    def context3Pressed(self, event: 'QKeyEvent') -> None: ...
    def context2Pressed(self, event: 'QKeyEvent') -> None: ...
    def context1Pressed(self, event: 'QKeyEvent') -> None: ...
    def noPressed(self, event: 'QKeyEvent') -> None: ...
    def yesPressed(self, event: 'QKeyEvent') -> None: ...
    def selectPressed(self, event: 'QKeyEvent') -> None: ...
    def cancelPressed(self, event: 'QKeyEvent') -> None: ...
    def backPressed(self, event: 'QKeyEvent') -> None: ...
    def spacePressed(self, event: 'QKeyEvent') -> None: ...
    def deletePressed(self, event: 'QKeyEvent') -> None: ...
    def enterPressed(self, event: 'QKeyEvent') -> None: ...
    def returnPressed(self, event: 'QKeyEvent') -> None: ...
    def escapePressed(self, event: 'QKeyEvent') -> None: ...
    def numberSignPressed(self, event: 'QKeyEvent') -> None: ...
    def asteriskPressed(self, event: 'QKeyEvent') -> None: ...
    def backtabPressed(self, event: 'QKeyEvent') -> None: ...
    def tabPressed(self, event: 'QKeyEvent') -> None: ...
    def downPressed(self, event: 'QKeyEvent') -> None: ...
    def upPressed(self, event: 'QKeyEvent') -> None: ...
    def rightPressed(self, event: 'QKeyEvent') -> None: ...
    def leftPressed(self, event: 'QKeyEvent') -> None: ...
    def digit9Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit8Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit7Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit6Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit5Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit4Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit3Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit2Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit1Pressed(self, event: 'QKeyEvent') -> None: ...
    def digit0Pressed(self, event: 'QKeyEvent') -> None: ...
    def focusChanged(self, focus: bool) -> None: ...
    def sourceDeviceChanged(self, keyboardDevice: 'QKeyboardDevice') -> None: ...
    def setFocus(self, focus: bool) -> None: ...
    def setSourceDevice(self, keyboardDevice: 'QKeyboardDevice') -> None: ...
    def focus(self) -> bool: ...
    def sourceDevice(self) -> 'QKeyboardDevice': ...

class QKeyEvent(QtCore.QObject):

    @typing.overload
    def __init__(self, type: QtCore.QEvent.Type, key: int, modifiers: typing.Union[QtCore.Qt.KeyboardModifiers, QtCore.Qt.KeyboardModifier], text: str = ..., autorep: bool = ..., count: int = ...) -> None: ...
    @typing.overload
    def __init__(self, ke: QtGui.QKeyEvent) -> None: ...

    def matches(self, key_: QtGui.QKeySequence.StandardKey) -> bool: ...
    def type(self) -> QtCore.QEvent.Type: ...
    def setAccepted(self, accepted: bool) -> None: ...
    def isAccepted(self) -> bool: ...
    def nativeScanCode(self) -> int: ...
    def count(self) -> int: ...
    def isAutoRepeat(self) -> bool: ...
    def modifiers(self) -> int: ...
    def text(self) -> str: ...
    def key(self) -> int: ...

class QLogicalDevice(Qt3DCore.QComponent):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def axes(self) -> typing.List['QAxis']: ...
    def removeAxis(self, axis: 'QAxis') -> None: ...
    def addAxis(self, axis: 'QAxis') -> None: ...
    def actions(self) -> typing.List['QAction']: ...
    def removeAction(self, action: 'QAction') -> None: ...
    def addAction(self, action: 'QAction') -> None: ...

class QMouseDevice('QAbstractPhysicalDevice'):

    class Axis(int):
        X = ... # type: QMouseDevice.Axis
        Y = ... # type: QMouseDevice.Axis
        WheelX = ... # type: QMouseDevice.Axis
        WheelY = ... # type: QMouseDevice.Axis

    X = ...  # type: QMouseDevice.Axis
    Y = ...  # type: QMouseDevice.Axis
    WheelX = ...  # type: QMouseDevice.Axis
    WheelY = ...  # type: QMouseDevice.Axis

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def updateAxesContinuouslyChanged(self, updateAxesContinuously: bool) -> None: ...
    def setUpdateAxesContinuously(self, updateAxesContinuously: bool) -> None: ...
    def updateAxesContinuously(self) -> bool: ...
    def sceneChangeEvent(self, change: Qt3DCore.QSceneChange) -> None: ...
    def sensitivityChanged(self, value: float) -> None: ...
    def setSensitivity(self, value: float) -> None: ...
    def sensitivity(self) -> float: ...
    def buttonIdentifier(self, name: str) -> int: ...
    def axisIdentifier(self, name: str) -> int: ...
    def buttonNames(self) -> typing.List[str]: ...
    def axisNames(self) -> typing.List[str]: ...
    def buttonCount(self) -> int: ...
    def axisCount(self) -> int: ...

class QMouseEvent(QtCore.QObject):

    class Modifiers(int):
        NoModifier = ... # type: QMouseEvent.Modifiers
        ShiftModifier = ... # type: QMouseEvent.Modifiers
        ControlModifier = ... # type: QMouseEvent.Modifiers
        AltModifier = ... # type: QMouseEvent.Modifiers
        MetaModifier = ... # type: QMouseEvent.Modifiers
        KeypadModifier = ... # type: QMouseEvent.Modifiers

    NoModifier = ...  # type: QMouseEvent.Modifiers
    ShiftModifier = ...  # type: QMouseEvent.Modifiers
    ControlModifier = ...  # type: QMouseEvent.Modifiers
    AltModifier = ...  # type: QMouseEvent.Modifiers
    MetaModifier = ...  # type: QMouseEvent.Modifiers
    KeypadModifier = ...  # type: QMouseEvent.Modifiers

    class Buttons(int):
        LeftButton = ... # type: QMouseEvent.Buttons
        RightButton = ... # type: QMouseEvent.Buttons
        MiddleButton = ... # type: QMouseEvent.Buttons
        BackButton = ... # type: QMouseEvent.Buttons
        NoButton = ... # type: QMouseEvent.Buttons

    LeftButton = ...  # type: QMouseEvent.Buttons
    RightButton = ...  # type: QMouseEvent.Buttons
    MiddleButton = ...  # type: QMouseEvent.Buttons
    BackButton = ...  # type: QMouseEvent.Buttons
    NoButton = ...  # type: QMouseEvent.Buttons

    def __init__(self, e: QtGui.QMouseEvent) -> None: ...

    def type(self) -> QtCore.QEvent.Type: ...
    def setAccepted(self, accepted: bool) -> None: ...
    def isAccepted(self) -> bool: ...
    def modifiers(self) -> 'QMouseEvent.Modifiers': ...
    def buttons(self) -> int: ...
    def button(self) -> 'QMouseEvent.Buttons': ...
    def wasHeld(self) -> bool: ...
    def y(self) -> int: ...
    def x(self) -> int: ...

class QWheelEvent(QtCore.QObject):

    class Modifiers(int):
        NoModifier = ... # type: QWheelEvent.Modifiers
        ShiftModifier = ... # type: QWheelEvent.Modifiers
        ControlModifier = ... # type: QWheelEvent.Modifiers
        AltModifier = ... # type: QWheelEvent.Modifiers
        MetaModifier = ... # type: QWheelEvent.Modifiers
        KeypadModifier = ... # type: QWheelEvent.Modifiers

    NoModifier = ...  # type: QWheelEvent.Modifiers
    ShiftModifier = ...  # type: QWheelEvent.Modifiers
    ControlModifier = ...  # type: QWheelEvent.Modifiers
    AltModifier = ...  # type: QWheelEvent.Modifiers
    MetaModifier = ...  # type: QWheelEvent.Modifiers
    KeypadModifier = ...  # type: QWheelEvent.Modifiers

    class Buttons(int):
        LeftButton = ... # type: QWheelEvent.Buttons
        RightButton = ... # type: QWheelEvent.Buttons
        MiddleButton = ... # type: QWheelEvent.Buttons
        BackButton = ... # type: QWheelEvent.Buttons
        NoButton = ... # type: QWheelEvent.Buttons

    LeftButton = ...  # type: QWheelEvent.Buttons
    RightButton = ...  # type: QWheelEvent.Buttons
    MiddleButton = ...  # type: QWheelEvent.Buttons
    BackButton = ...  # type: QWheelEvent.Buttons
    NoButton = ...  # type: QWheelEvent.Buttons

    def __init__(self, e: QtGui.QWheelEvent) -> None: ...

    def type(self) -> QtCore.QEvent.Type: ...
    def setAccepted(self, accepted: bool) -> None: ...
    def isAccepted(self) -> bool: ...
    def modifiers(self) -> 'QWheelEvent.Modifiers': ...
    def buttons(self) -> int: ...
    def angleDelta(self) -> QtCore.QPoint: ...
    def y(self) -> int: ...
    def x(self) -> int: ...

class QMouseHandler(Qt3DCore.QComponent):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def sceneChangeEvent(self, change: Qt3DCore.QSceneChange) -> None: ...
    def wheel(self, wheel: 'QWheelEvent') -> None: ...
    def positionChanged(self, mouse: 'QMouseEvent') -> None: ...
    def pressAndHold(self, mouse: 'QMouseEvent') -> None: ...
    def released(self, mouse: 'QMouseEvent') -> None: ...
    def pressed(self, mouse: 'QMouseEvent') -> None: ...
    def exited(self) -> None: ...
    def entered(self) -> None: ...
    def doubleClicked(self, mouse: 'QMouseEvent') -> None: ...
    def clicked(self, mouse: 'QMouseEvent') -> None: ...
    def containsMouseChanged(self, containsMouse: bool) -> None: ...
    def sourceDeviceChanged(self, mouseDevice: 'QMouseDevice') -> None: ...
    def setSourceDevice(self, mouseDevice: 'QMouseDevice') -> None: ...
    def containsMouse(self) -> bool: ...
    def sourceDevice(self) -> 'QMouseDevice': ...

class QPhysicalDeviceCreatedChangeBase(Qt3DCore.QNodeCreatedChangeBase):

    def __init__(self, device: 'QAbstractPhysicalDevice') -> None: ...

    def axisSettingIds(self) -> typing.List[Qt3DCore.QNodeId]: ...
