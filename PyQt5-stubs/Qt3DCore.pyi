# The PEP 484 type hints stub file for the Qt3DCore module.
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

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

# Convenient aliases for complicated OpenGL types.
PYQT_OPENGL_ARRAY = typing.Union[typing.Sequence[int], typing.Sequence[float],
        sip.Buffer, None]
PYQT_OPENGL_BOUND_ARRAY = typing.Union[typing.Sequence[int],
        typing.Sequence[float], sip.Buffer, int, None]


class ChangeFlag(int):
    NodeCreated = ... # type: ChangeFlag
    NodeDeleted = ... # type: ChangeFlag
    PropertyUpdated = ... # type: ChangeFlag
    PropertyValueAdded = ... # type: ChangeFlag
    PropertyValueRemoved = ... # type: ChangeFlag
    ComponentAdded = ... # type: ChangeFlag
    ComponentRemoved = ... # type: ChangeFlag
    CommandRequested = ... # type: ChangeFlag
    CallbackTriggered = ... # type: ChangeFlag
    AllChanges = ... # type: ChangeFlag

class QAbstractAspect(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def unregisterBackendType(self, a0: QtCore.QMetaObject) -> None: ...
    @typing.overload
    def registerBackendType(self, a0: QtCore.QMetaObject, functor: 'QBackendNodeMapper') -> None: ...
    @typing.overload
    def registerBackendType(self, obj: QtCore.QMetaObject, functor: 'QBackendNodeMapper', supportsSyncing: bool) -> None: ...
    def rootEntityId(self) -> 'QNodeId': ...

class QAspectEngine(QtCore.QObject):

    class RunMode(int):
        Manual = ... # type: QAspectEngine.RunMode
        Automatic = ... # type: QAspectEngine.RunMode

    Manual = ...  # type: QAspectEngine.RunMode
    Automatic = ...  # type: QAspectEngine.RunMode

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    def processFrame(self) -> None: ...
    def runMode(self) -> 'QAspectEngine.RunMode': ...
    def setRunMode(self, mode: 'QAspectEngine.RunMode') -> None: ...
    def executeCommand(self, command: str) -> typing.Any: ...
    def aspects(self) -> typing.List['QAbstractAspect']: ...
    @typing.overload
    def unregisterAspect(self, aspect: 'QAbstractAspect') -> None: ...
    @typing.overload
    def unregisterAspect(self, name: str) -> None: ...
    @typing.overload
    def registerAspect(self, aspect: 'QAbstractAspect') -> None: ...
    @typing.overload
    def registerAspect(self, name: str) -> None: ...
    def rootEntity(self) -> 'QEntity': ...
    def setRootEntity(self, root: 'QEntity') -> None: ...

class QNode(QtCore.QObject):

    class PropertyTrackingMode(int):
        TrackFinalValues = ... # type: QNode.PropertyTrackingMode
        DontTrackValues = ... # type: QNode.PropertyTrackingMode
        TrackAllValues = ... # type: QNode.PropertyTrackingMode

    TrackFinalValues = ...  # type: QNode.PropertyTrackingMode
    DontTrackValues = ...  # type: QNode.PropertyTrackingMode
    TrackAllValues = ...  # type: QNode.PropertyTrackingMode

    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...

    def sendReply(self, command: 'QNodeCommand') -> None: ...
    def sendCommand(self, name: str, data: typing.Any = ..., replyTo: int = ...) -> int: ...
    def defaultPropertyTrackingModeChanged(self, mode: 'QNode.PropertyTrackingMode') -> None: ...
    def setDefaultPropertyTrackingMode(self, mode: 'QNode.PropertyTrackingMode') -> None: ...
    def clearPropertyTrackings(self) -> None: ...
    def clearPropertyTracking(self, propertyName: str) -> None: ...
    def propertyTracking(self, propertyName: str) -> 'QNode.PropertyTrackingMode': ...
    def setPropertyTracking(self, propertyName: str, trackMode: 'QNode.PropertyTrackingMode') -> None: ...
    def defaultPropertyTrackingMode(self) -> 'QNode.PropertyTrackingMode': ...
    def sceneChangeEvent(self, change: 'QSceneChange') -> None: ...
    def notifyObservers(self, change: 'QSceneChange') -> None: ...
    def nodeDestroyed(self) -> None: ...
    def enabledChanged(self, enabled: bool) -> None: ...
    def parentChanged(self, parent: QtCore.QObject) -> None: ...
    def setEnabled(self, isEnabled: bool) -> None: ...
    def setParent(self, parent: 'QNode') -> None: ...  # type: ignore[override]
    def isEnabled(self) -> bool: ...
    def childNodes(self) -> typing.List['QNode']: ...
    def blockNotifications(self, block: bool) -> bool: ...
    def notificationsBlocked(self) -> bool: ...
    def parentNode(self) -> 'QNode': ...
    def id(self) -> 'QNodeId': ...

class QAbstractSkeleton('QNode'):

    def sceneChangeEvent(self, change: 'QSceneChange') -> None: ...
    def jointCountChanged(self, jointCount: int) -> None: ...
    def jointCount(self) -> int: ...

class QComponent('QNode'):

    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...

    def removedFromEntity(self, entity: 'QEntity') -> None: ...
    def addedToEntity(self, entity: 'QEntity') -> None: ...
    def shareableChanged(self, isShareable: bool) -> None: ...
    def setShareable(self, isShareable: bool) -> None: ...
    def entities(self) -> typing.List['QEntity']: ...
    def isShareable(self) -> bool: ...

class QArmature('QComponent'):

    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...

    def skeletonChanged(self, skeleton: 'QAbstractSkeleton') -> None: ...
    def setSkeleton(self, skeleton: 'QAbstractSkeleton') -> None: ...
    def skeleton(self) -> 'QAbstractSkeleton': ...

class QBackendNodeMapper(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QBackendNodeMapper') -> None: ...

    def destroy(self, id: 'QNodeId') -> None: ...
    def get(self, id: 'QNodeId') -> 'QBackendNode': ...
    def create(self, change: 'QNodeCreatedChangeBase') -> 'QBackendNode': ...

class QBackendNode(sip.simplewrapper):

    class Mode(int):
        ReadOnly = ... # type: QBackendNode.Mode
        ReadWrite = ... # type: QBackendNode.Mode

    ReadOnly = ...  # type: QBackendNode.Mode
    ReadWrite = ...  # type: QBackendNode.Mode

    def __init__(self, mode: 'QBackendNode.Mode' = ...) -> None: ...

    def sendReply(self, command: 'QNodeCommand') -> None: ...
    def sendCommand(self, name: str, data: typing.Any, replyTo: int = ...) -> int: ...
    def sceneChangeEvent(self, e: 'QSceneChange') -> None: ...
    def notifyObservers(self, e: 'QSceneChange') -> None: ...
    def mode(self) -> 'QBackendNode.Mode': ...
    def isEnabled(self) -> bool: ...
    def setEnabled(self, enabled: bool) -> None: ...
    def peerId(self) -> 'QNodeId': ...

class QSceneChange(sip.simplewrapper):

    class DeliveryFlag(int):
        BackendNodes = ... # type: QSceneChange.DeliveryFlag
        Nodes = ... # type: QSceneChange.DeliveryFlag
        DeliverToAll = ... # type: QSceneChange.DeliveryFlag

    BackendNodes = ...  # type: QSceneChange.DeliveryFlag
    Nodes = ...  # type: QSceneChange.DeliveryFlag
    DeliverToAll = ...  # type: QSceneChange.DeliveryFlag

    class DeliveryFlags(sip.simplewrapper):

        @typing.overload
        def __init__(self) -> None: ...
        @typing.overload
        def __init__(self, f: typing.Union['QSceneChange.DeliveryFlags', 'QSceneChange.DeliveryFlag']) -> None: ...
        @typing.overload
        def __init__(self, a0: 'QSceneChange.DeliveryFlags') -> None: ...

        def __hash__(self) -> int: ...
        def __bool__(self) -> int: ...
        def __invert__(self) -> 'QSceneChange.DeliveryFlags': ...
        def __index__(self) -> int: ...
        def __int__(self) -> int: ...

    def __init__(self, type: 'ChangeFlag', subjectId: 'QNodeId') -> None: ...

    def subjectId(self) -> 'QNodeId': ...
    def deliveryFlags(self) -> 'QSceneChange.DeliveryFlags': ...
    def setDeliveryFlags(self, flags: typing.Union['QSceneChange.DeliveryFlags', 'QSceneChange.DeliveryFlag']) -> None: ...
    def type(self) -> 'ChangeFlag': ...

class QComponentAddedChange('QSceneChange'):

    @typing.overload
    def __init__(self, entity: 'QEntity', component: 'QComponent') -> None: ...
    @typing.overload
    def __init__(self, component: 'QComponent', entity: 'QEntity') -> None: ...

    def componentMetaObject(self) -> QtCore.QMetaObject: ...
    def componentId(self) -> 'QNodeId': ...
    def entityId(self) -> 'QNodeId': ...

class QComponentRemovedChange('QSceneChange'):

    @typing.overload
    def __init__(self, entity: 'QEntity', component: 'QComponent') -> None: ...
    @typing.overload
    def __init__(self, component: 'QComponent', entity: 'QEntity') -> None: ...

    def componentMetaObject(self) -> QtCore.QMetaObject: ...
    def componentId(self) -> 'QNodeId': ...
    def entityId(self) -> 'QNodeId': ...

class QPropertyUpdatedChangeBase('QSceneChange'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

class QDynamicPropertyUpdatedChange('QPropertyUpdatedChangeBase'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

    def setValue(self, value: typing.Any) -> None: ...
    def value(self) -> typing.Any: ...
    def setPropertyName(self, name: typing.Union[QtCore.QByteArray, bytes, bytearray]) -> None: ...
    def propertyName(self) -> QtCore.QByteArray: ...

class QEntity('QNode'):

    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...

    def parentEntity(self) -> 'QEntity': ...
    def removeComponent(self, comp: 'QComponent') -> None: ...
    def addComponent(self, comp: 'QComponent') -> None: ...
    def components(self) -> typing.List['QComponent']: ...

class QJoint('QNode'):

    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...

    def nameChanged(self, name: str) -> None: ...
    def rotationZChanged(self, rotationZ: float) -> None: ...
    def rotationYChanged(self, rotationY: float) -> None: ...
    def rotationXChanged(self, rotationX: float) -> None: ...
    def inverseBindMatrixChanged(self, inverseBindMatrix: QtGui.QMatrix4x4) -> None: ...
    def translationChanged(self, translation: QtGui.QVector3D) -> None: ...
    def rotationChanged(self, rotation: QtGui.QQuaternion) -> None: ...
    def scaleChanged(self, scale: QtGui.QVector3D) -> None: ...
    def setToIdentity(self) -> None: ...
    def setName(self, name: str) -> None: ...
    def setRotationZ(self, rotationZ: float) -> None: ...
    def setRotationY(self, rotationY: float) -> None: ...
    def setRotationX(self, rotationX: float) -> None: ...
    def setInverseBindMatrix(self, inverseBindMatrix: QtGui.QMatrix4x4) -> None: ...
    def setTranslation(self, translation: QtGui.QVector3D) -> None: ...
    def setRotation(self, rotation: QtGui.QQuaternion) -> None: ...
    def setScale(self, scale: QtGui.QVector3D) -> None: ...
    def childJoints(self) -> typing.List['QJoint']: ...
    def removeChildJoint(self, joint: 'QJoint') -> None: ...
    def addChildJoint(self, joint: 'QJoint') -> None: ...
    def name(self) -> str: ...
    def rotationZ(self) -> float: ...
    def rotationY(self) -> float: ...
    def rotationX(self) -> float: ...
    def inverseBindMatrix(self) -> QtGui.QMatrix4x4: ...
    def translation(self) -> QtGui.QVector3D: ...
    def rotation(self) -> QtGui.QQuaternion: ...
    def scale(self) -> QtGui.QVector3D: ...

class QNodeIdTypePair(sip.simplewrapper):

    id = ... # type: 'QNodeId'
    type = ... # type: QtCore.QMetaObject

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, _id: 'QNodeId', _type: QtCore.QMetaObject) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QNodeIdTypePair') -> None: ...

class QNodeCommand('QSceneChange'):

    def __init__(self, id: 'QNodeId') -> None: ...

    def setReplyToCommandId(self, id: int) -> None: ...
    def inReplyTo(self) -> int: ...
    def setData(self, data: typing.Any) -> None: ...
    def data(self) -> typing.Any: ...
    def setName(self, name: str) -> None: ...
    def name(self) -> str: ...
    def commandId(self) -> int: ...

class QNodeCreatedChangeBase('QSceneChange'):

    def __init__(self, node: 'QNode') -> None: ...

    def isNodeEnabled(self) -> bool: ...
    def metaObject(self) -> QtCore.QMetaObject: ...
    def parentId(self) -> 'QNodeId': ...

class QNodeDestroyedChange('QSceneChange'):

    def __init__(self, node: 'QNode', subtreeIdsAndTypes: typing.Iterable['QNodeIdTypePair']) -> None: ...

    def subtreeIdsAndTypes(self) -> typing.List['QNodeIdTypePair']: ...

class QNodeId(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QNodeId') -> None: ...

    def __hash__(self) -> int: ...
    def __int__(self) -> bool: ...
    def id(self) -> int: ...
    def isNull(self) -> bool: ...
    @staticmethod
    def createId() -> 'QNodeId': ...

class QPropertyValueAddedChangeBase('QSceneChange'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

class QStaticPropertyValueAddedChangeBase('QPropertyValueAddedChangeBase'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

    def setPropertyName(self, name: str) -> None: ...
    def propertyName(self) -> str: ...

class QPropertyNodeAddedChange('QStaticPropertyValueAddedChangeBase'):

    def __init__(self, subjectId: 'QNodeId', node: 'QNode') -> None: ...

    def metaObject(self) -> QtCore.QMetaObject: ...
    def addedNodeId(self) -> 'QNodeId': ...

class QPropertyValueRemovedChangeBase('QSceneChange'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

class QStaticPropertyValueRemovedChangeBase('QPropertyValueRemovedChangeBase'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

    def setPropertyName(self, name: str) -> None: ...
    def propertyName(self) -> str: ...

class QPropertyNodeRemovedChange('QStaticPropertyValueRemovedChangeBase'):

    def __init__(self, subjectId: 'QNodeId', node: 'QNode') -> None: ...

    def metaObject(self) -> QtCore.QMetaObject: ...
    def removedNodeId(self) -> 'QNodeId': ...

class QStaticPropertyUpdatedChangeBase('QPropertyUpdatedChangeBase'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

    def setPropertyName(self, name: str) -> None: ...
    def propertyName(self) -> str: ...

class QPropertyUpdatedChange('QStaticPropertyUpdatedChangeBase'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

    def setValue(self, value: typing.Any) -> None: ...
    def value(self) -> typing.Any: ...

class QPropertyValueAddedChange('QStaticPropertyValueAddedChangeBase'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

    def addedValue(self) -> typing.Any: ...
    def setAddedValue(self, value: typing.Any) -> None: ...

class QPropertyValueRemovedChange('QStaticPropertyValueRemovedChangeBase'):

    def __init__(self, subjectId: 'QNodeId') -> None: ...

    def removedValue(self) -> typing.Any: ...
    def setRemovedValue(self, value: typing.Any) -> None: ...

class ChangeFlags(sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, f: typing.Union['ChangeFlags', 'ChangeFlag']) -> None: ...
    @typing.overload
    def __init__(self, a0: 'ChangeFlags') -> None: ...

    def __hash__(self) -> int: ...
    def __bool__(self) -> int: ...
    def __invert__(self) -> 'ChangeFlags': ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...

class QSkeleton('QAbstractSkeleton'):

    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...

    def rootJointChanged(self, rootJoint: 'QJoint') -> None: ...
    def setRootJoint(self, rootJoint: 'QJoint') -> None: ...
    def rootJoint(self) -> 'QJoint': ...

class QSkeletonLoader('QAbstractSkeleton'):

    class Status(int):
        NotReady = ... # type: QSkeletonLoader.Status
        Ready = ... # type: QSkeletonLoader.Status
        Error = ... # type: QSkeletonLoader.Status

    NotReady = ...  # type: QSkeletonLoader.Status
    Ready = ...  # type: QSkeletonLoader.Status
    Error = ...  # type: QSkeletonLoader.Status

    @typing.overload
    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...
    @typing.overload
    def __init__(self, source: QtCore.QUrl, parent: typing.Optional['QNode'] = ...) -> None: ...

    def sceneChangeEvent(self, change: 'QSceneChange') -> None: ...
    def rootJointChanged(self, rootJoint: 'QJoint') -> None: ...
    def createJointsEnabledChanged(self, createJointsEnabled: bool) -> None: ...
    def statusChanged(self, status: 'QSkeletonLoader.Status') -> None: ...
    def sourceChanged(self, source: QtCore.QUrl) -> None: ...
    def setCreateJointsEnabled(self, enabled: bool) -> None: ...
    def setSource(self, source: QtCore.QUrl) -> None: ...
    def rootJoint(self) -> 'QJoint': ...
    def isCreateJointsEnabled(self) -> bool: ...
    def status(self) -> 'QSkeletonLoader.Status': ...
    def source(self) -> QtCore.QUrl: ...

class QTransform('QComponent'):

    def __init__(self, parent: typing.Optional['QNode'] = ...) -> None: ...

    def sceneChangeEvent(self, change: 'QSceneChange') -> None: ...
    def worldMatrixChanged(self, worldMatrix: QtGui.QMatrix4x4) -> None: ...
    def worldMatrix(self) -> QtGui.QMatrix4x4: ...
    def rotationZChanged(self, rotationZ: float) -> None: ...
    def rotationYChanged(self, rotationY: float) -> None: ...
    def rotationXChanged(self, rotationX: float) -> None: ...
    def matrixChanged(self) -> None: ...
    def translationChanged(self, translation: QtGui.QVector3D) -> None: ...
    def rotationChanged(self, rotation: QtGui.QQuaternion) -> None: ...
    def scale3DChanged(self, scale: QtGui.QVector3D) -> None: ...
    def scaleChanged(self, scale: float) -> None: ...
    def setRotationZ(self, rotationZ: float) -> None: ...
    def setRotationY(self, rotationY: float) -> None: ...
    def setRotationX(self, rotationX: float) -> None: ...
    def setMatrix(self, matrix: QtGui.QMatrix4x4) -> None: ...
    def setTranslation(self, translation: QtGui.QVector3D) -> None: ...
    def setRotation(self, rotation: QtGui.QQuaternion) -> None: ...
    def setScale3D(self, scale: QtGui.QVector3D) -> None: ...
    def setScale(self, scale: float) -> None: ...
    def rotationZ(self) -> float: ...
    def rotationY(self) -> float: ...
    def rotationX(self) -> float: ...
    def matrix(self) -> QtGui.QMatrix4x4: ...
    @staticmethod
    def rotateFromAxes(xAxis: QtGui.QVector3D, yAxis: QtGui.QVector3D, zAxis: QtGui.QVector3D) -> QtGui.QMatrix4x4: ...
    @staticmethod
    def rotateAround(point: QtGui.QVector3D, angle: float, axis: QtGui.QVector3D) -> QtGui.QMatrix4x4: ...
    @typing.overload
    @staticmethod
    def fromEulerAngles(eulerAngles: QtGui.QVector3D) -> QtGui.QQuaternion: ...
    @typing.overload
    @staticmethod
    def fromEulerAngles(pitch: float, yaw: float, roll: float) -> QtGui.QQuaternion: ...
    @typing.overload
    @staticmethod
    def fromAxesAndAngles(axis1: QtGui.QVector3D, angle1: float, axis2: QtGui.QVector3D, angle2: float) -> QtGui.QQuaternion: ...
    @typing.overload
    @staticmethod
    def fromAxesAndAngles(axis1: QtGui.QVector3D, angle1: float, axis2: QtGui.QVector3D, angle2: float, axis3: QtGui.QVector3D, angle3: float) -> QtGui.QQuaternion: ...
    @typing.overload
    @staticmethod
    def fromAxisAndAngle(axis: QtGui.QVector3D, angle: float) -> QtGui.QQuaternion: ...
    @typing.overload
    @staticmethod
    def fromAxisAndAngle(x: float, y: float, z: float, angle: float) -> QtGui.QQuaternion: ...
    @staticmethod
    def fromAxes(xAxis: QtGui.QVector3D, yAxis: QtGui.QVector3D, zAxis: QtGui.QVector3D) -> QtGui.QQuaternion: ...
    def translation(self) -> QtGui.QVector3D: ...
    def rotation(self) -> QtGui.QQuaternion: ...
    def scale3D(self) -> QtGui.QVector3D: ...
    def scale(self) -> float: ...

def qIdForNode(node: 'QNode') -> 'QNodeId': ...
