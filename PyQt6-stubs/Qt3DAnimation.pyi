# The PEP 484 type hints stub file for the Qt3DAnimation module.
#
# Generated by SIP 6.2.0
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
# 
# This file is part of PyQt6-3D.
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
from PyQt6 import QtCore
from PyQt6 import Qt3DRender
from PyQt6 import Qt3DCore

# Support for QDate, QDateTime and QTime.
import datetime

# Convenient type aliases.
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]


class QAbstractAnimation(QtCore.QObject):

    class AnimationType(enum.Enum):
        KeyframeAnimation = ... # type: QAbstractAnimation.AnimationType
        MorphingAnimation = ... # type: QAbstractAnimation.AnimationType
        VertexBlendAnimation = ... # type: QAbstractAnimation.AnimationType

    KeyframeAnimation = ...  # type: QAbstractAnimation.AnimationType
    MorphingAnimation = ...  # type: QAbstractAnimation.AnimationType
    VertexBlendAnimation = ...  # type: QAbstractAnimation.AnimationType

    durationChanged: typing.ClassVar[QtCore.pyqtSignal]
    positionChanged: typing.ClassVar[QtCore.pyqtSignal]
    animationNameChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setDuration(self, duration: float) -> None: ...
    def setPosition(self, position: float) -> None: ...
    def setAnimationName(self, name: str) -> None: ...
    def duration(self) -> float: ...
    def position(self) -> float: ...
    def animationType(self) -> 'QAbstractAnimation.AnimationType': ...
    def animationName(self) -> str: ...

class QAbstractAnimationClip(Qt3DCore.QNode):

    durationChanged: typing.ClassVar[QtCore.pyqtSignal]
    def duration(self) -> float: ...

class QAbstractChannelMapping(Qt3DCore.QNode): ...

class QAbstractClipAnimator(Qt3DCore.QComponent):

    class Loops(enum.Enum):
        Infinite = ... # type: QAbstractClipAnimator.Loops

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    normalizedTimeChanged: typing.ClassVar[QtCore.pyqtSignal]
    clockChanged: typing.ClassVar[QtCore.pyqtSignal]
    loopCountChanged: typing.ClassVar[QtCore.pyqtSignal]
    channelMapperChanged: typing.ClassVar[QtCore.pyqtSignal]
    runningChanged: typing.ClassVar[QtCore.pyqtSignal]
    def stop(self) -> None: ...
    def start(self) -> None: ...
    def setNormalizedTime(self, timeFraction: float) -> None: ...
    def setClock(self, clock: 'QClock') -> None: ...
    def setLoopCount(self, loops: int) -> None: ...
    def setChannelMapper(self, channelMapper: 'QChannelMapper') -> None: ...
    def setRunning(self, running: bool) -> None: ...
    def normalizedTime(self) -> float: ...
    def clock(self) -> 'QClock': ...
    def loopCount(self) -> int: ...
    def channelMapper(self) -> 'QChannelMapper': ...
    def isRunning(self) -> bool: ...

class QAbstractClipBlendNode(Qt3DCore.QNode):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

class QAdditiveClipBlend('QAbstractClipBlendNode'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    additiveClipChanged: typing.ClassVar[QtCore.pyqtSignal]
    baseClipChanged: typing.ClassVar[QtCore.pyqtSignal]
    additiveFactorChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setAdditiveClip(self, additiveClip: 'QAbstractClipBlendNode') -> None: ...
    def setBaseClip(self, baseClip: 'QAbstractClipBlendNode') -> None: ...
    def setAdditiveFactor(self, additiveFactor: float) -> None: ...
    def additiveClip(self) -> 'QAbstractClipBlendNode': ...
    def baseClip(self) -> 'QAbstractClipBlendNode': ...
    def additiveFactor(self) -> float: ...

class QAnimationAspect(Qt3DCore.QAbstractAspect):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

class QAnimationClip('QAbstractAnimationClip'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    clipDataChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setClipData(self, clipData: 'QAnimationClipData') -> None: ...
    def clipData(self) -> 'QAnimationClipData': ...


class QAnimationClipData(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QAnimationClipData') -> None: ...

    def isValid(self) -> bool: ...
    def clearChannels(self) -> None: ...
    def removeChannel(self, index: int) -> None: ...
    def insertChannel(self, index: int, c: 'QChannel') -> None: ...
    def appendChannel(self, c: 'QChannel') -> None: ...
    def channelCount(self) -> int: ...
    def name(self) -> str: ...
    def setName(self, name: str) -> None: ...

class QAnimationClipLoader('QAbstractAnimationClip'):

    class Status(enum.Enum):
        NotReady = ... # type: QAnimationClipLoader.Status
        Ready = ... # type: QAnimationClipLoader.Status
        Error = ... # type: QAnimationClipLoader.Status

    @typing.overload
    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...
    @typing.overload
    def __init__(self, source: QtCore.QUrl, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    statusChanged: typing.ClassVar[QtCore.pyqtSignal]
    sourceChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setSource(self, source: QtCore.QUrl) -> None: ...
    def status(self) -> 'QAnimationClipLoader.Status': ...
    def source(self) -> QtCore.QUrl: ...

class QAnimationController(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    recursiveChanged: typing.ClassVar[QtCore.pyqtSignal]
    entityChanged: typing.ClassVar[QtCore.pyqtSignal]
    positionOffsetChanged: typing.ClassVar[QtCore.pyqtSignal]
    positionScaleChanged: typing.ClassVar[QtCore.pyqtSignal]
    positionChanged: typing.ClassVar[QtCore.pyqtSignal]
    activeAnimationGroupChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setRecursive(self, recursive: bool) -> None: ...
    def setEntity(self, entity: Qt3DCore.QEntity) -> None: ...
    def setPositionOffset(self, offset: float) -> None: ...
    def setPositionScale(self, scale: float) -> None: ...
    def setPosition(self, position: float) -> None: ...
    def setActiveAnimationGroup(self, index: int) -> None: ...
    def getGroup(self, index: int) -> 'QAnimationGroup': ...
    def getAnimationIndex(self, name: str) -> int: ...
    def removeAnimationGroup(self, animationGroups: 'QAnimationGroup') -> None: ...
    def addAnimationGroup(self, animationGroups: 'QAnimationGroup') -> None: ...
    def setAnimationGroups(self, animationGroups: typing.Iterable['QAnimationGroup']) -> None: ...
    def recursive(self) -> bool: ...
    def entity(self) -> Qt3DCore.QEntity: ...
    def positionOffset(self) -> float: ...
    def positionScale(self) -> float: ...
    def position(self) -> float: ...
    def activeAnimationGroup(self) -> int: ...
    def animationGroupList(self) -> typing.List['QAnimationGroup']: ...

class QAnimationGroup(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    durationChanged: typing.ClassVar[QtCore.pyqtSignal]
    positionChanged: typing.ClassVar[QtCore.pyqtSignal]
    nameChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setPosition(self, position: float) -> None: ...
    def setName(self, name: str) -> None: ...
    def removeAnimation(self, animation: 'QAbstractAnimation') -> None: ...
    def addAnimation(self, animation: 'QAbstractAnimation') -> None: ...
    def setAnimations(self, animations: typing.Iterable['QAbstractAnimation']) -> None: ...
    def duration(self) -> float: ...
    def position(self) -> float: ...
    def animationList(self) -> typing.List['QAbstractAnimation']: ...
    def name(self) -> str: ...

class QBlendedClipAnimator('QAbstractClipAnimator'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    blendTreeChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setBlendTree(self, blendTree: 'QAbstractClipBlendNode') -> None: ...
    def blendTree(self) -> 'QAbstractClipBlendNode': ...


class QChannel(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QChannel') -> None: ...

    def clearChannelComponents(self) -> None: ...
    def removeChannelComponent(self, index: int) -> None: ...
    def insertChannelComponent(self, index: int, component: 'QChannelComponent') -> None: ...
    def appendChannelComponent(self, component: 'QChannelComponent') -> None: ...
    def channelComponentCount(self) -> int: ...
    def jointIndex(self) -> int: ...
    def setJointIndex(self, jointIndex: int) -> None: ...
    def name(self) -> str: ...
    def setName(self, name: str) -> None: ...


class QChannelComponent(PyQt6.sip.simplewrapper):

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, name: str) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QChannelComponent') -> None: ...

    def clearKeyFrames(self) -> None: ...
    def removeKeyFrame(self, index: int) -> None: ...
    def insertKeyFrame(self, index: int, kf: 'QKeyFrame') -> None: ...
    def appendKeyFrame(self, kf: 'QKeyFrame') -> None: ...
    def keyFrameCount(self) -> int: ...
    def name(self) -> str: ...
    def setName(self, name: str) -> None: ...

class QChannelMapper(Qt3DCore.QNode):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    def mappings(self) -> typing.List['QAbstractChannelMapping']: ...
    def removeMapping(self, mapping: 'QAbstractChannelMapping') -> None: ...
    def addMapping(self, mapping: 'QAbstractChannelMapping') -> None: ...

class QChannelMapping('QAbstractChannelMapping'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    propertyChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetChanged: typing.ClassVar[QtCore.pyqtSignal]
    channelNameChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setProperty(self, property: str) -> None: ...  # type: ignore[override]
    def setTarget(self, target: Qt3DCore.QNode) -> None: ...
    def setChannelName(self, channelName: str) -> None: ...
    def property(self) -> str: ...  # type: ignore[override]
    def target(self) -> Qt3DCore.QNode: ...
    def channelName(self) -> str: ...

class QClipAnimator('QAbstractClipAnimator'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    clipChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setClip(self, clip: 'QAbstractAnimationClip') -> None: ...
    def clip(self) -> 'QAbstractAnimationClip': ...


class QClipBlendValue('QAbstractClipBlendNode'):

    @typing.overload
    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...
    @typing.overload
    def __init__(self, clip: 'QAbstractAnimationClip', parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    clipChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setClip(self, clip: 'QAbstractAnimationClip') -> None: ...
    def clip(self) -> 'QAbstractAnimationClip': ...

class QClock(Qt3DCore.QNode):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    playbackRateChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setPlaybackRate(self, playbackRate: float) -> None: ...
    def playbackRate(self) -> float: ...


class QKeyFrame(PyQt6.sip.simplewrapper):

    class InterpolationType(enum.Enum):
        ConstantInterpolation = ... # type: QKeyFrame.InterpolationType
        LinearInterpolation = ... # type: QKeyFrame.InterpolationType
        BezierInterpolation = ... # type: QKeyFrame.InterpolationType

    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, coords: QtGui.QVector2D) -> None: ...
    @typing.overload
    def __init__(self, coords: QtGui.QVector2D, lh: QtGui.QVector2D, rh: QtGui.QVector2D) -> None: ...
    @typing.overload
    def __init__(self, a0: 'QKeyFrame') -> None: ...

    def interpolationType(self) -> 'QKeyFrame.InterpolationType': ...
    def setInterpolationType(self, interp: 'QKeyFrame.InterpolationType') -> None: ...
    def rightControlPoint(self) -> QtGui.QVector2D: ...
    def setRightControlPoint(self, rh: QtGui.QVector2D) -> None: ...
    def leftControlPoint(self) -> QtGui.QVector2D: ...
    def setLeftControlPoint(self, lh: QtGui.QVector2D) -> None: ...
    def coordinates(self) -> QtGui.QVector2D: ...
    def setCoordinates(self, coords: QtGui.QVector2D) -> None: ...

class QKeyframeAnimation('QAbstractAnimation'):

    class RepeatMode(enum.Enum):
        None_ = ... # type: QKeyframeAnimation.RepeatMode
        Constant = ... # type: QKeyframeAnimation.RepeatMode
        Repeat = ... # type: QKeyframeAnimation.RepeatMode

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    endModeChanged: typing.ClassVar[QtCore.pyqtSignal]
    startModeChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetNameChanged: typing.ClassVar[QtCore.pyqtSignal]
    easingChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetChanged: typing.ClassVar[QtCore.pyqtSignal]
    framePositionsChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setEndMode(self, mode: 'QKeyframeAnimation.RepeatMode') -> None: ...
    def setStartMode(self, mode: 'QKeyframeAnimation.RepeatMode') -> None: ...
    def setTargetName(self, name: str) -> None: ...
    def setEasing(self, easing: typing.Union[QtCore.QEasingCurve, QtCore.QEasingCurve.Type]) -> None: ...
    def setTarget(self, target: Qt3DCore.QTransform) -> None: ...
    def setFramePositions(self, positions: typing.Iterable[float]) -> None: ...
    def removeKeyframe(self, keyframe: Qt3DCore.QTransform) -> None: ...
    def addKeyframe(self, keyframe: Qt3DCore.QTransform) -> None: ...
    def setKeyframes(self, keyframes: typing.Iterable[Qt3DCore.QTransform]) -> None: ...
    def endMode(self) -> 'QKeyframeAnimation.RepeatMode': ...
    def startMode(self) -> 'QKeyframeAnimation.RepeatMode': ...
    def targetName(self) -> str: ...
    def easing(self) -> QtCore.QEasingCurve: ...
    def target(self) -> Qt3DCore.QTransform: ...
    def keyframeList(self) -> typing.List[Qt3DCore.QTransform]: ...
    def framePositions(self) -> typing.List[float]: ...

class QLerpClipBlend('QAbstractClipBlendNode'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    endClipChanged: typing.ClassVar[QtCore.pyqtSignal]
    startClipChanged: typing.ClassVar[QtCore.pyqtSignal]
    blendFactorChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setEndClip(self, endClip: 'QAbstractClipBlendNode') -> None: ...
    def setStartClip(self, startClip: 'QAbstractClipBlendNode') -> None: ...
    def setBlendFactor(self, blendFactor: float) -> None: ...
    def endClip(self) -> 'QAbstractClipBlendNode': ...
    def startClip(self) -> 'QAbstractClipBlendNode': ...
    def blendFactor(self) -> float: ...

class QMorphingAnimation('QAbstractAnimation'):

    class Method(enum.Enum):
        Normalized = ... # type: QMorphingAnimation.Method
        Relative = ... # type: QMorphingAnimation.Method

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    easingChanged: typing.ClassVar[QtCore.pyqtSignal]
    methodChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetNameChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetChanged: typing.ClassVar[QtCore.pyqtSignal]
    interpolatorChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetPositionsChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setEasing(self, easing: typing.Union[QtCore.QEasingCurve, QtCore.QEasingCurve.Type]) -> None: ...
    def setMethod(self, method: 'QMorphingAnimation.Method') -> None: ...
    def setTargetName(self, name: str) -> None: ...
    def setTarget(self, target: Qt3DRender.QGeometryRenderer) -> None: ...
    def setTargetPositions(self, targetPositions: typing.Iterable[float]) -> None: ...
    def morphTargetList(self) -> typing.List['QMorphTarget']: ...
    def getWeights(self, positionIndex: int) -> typing.List[float]: ...
    def setWeights(self, positionIndex: int, weights: typing.Iterable[float]) -> None: ...
    def removeMorphTarget(self, target: 'QMorphTarget') -> None: ...
    def addMorphTarget(self, target: 'QMorphTarget') -> None: ...
    def setMorphTargets(self, targets: typing.Iterable['QMorphTarget']) -> None: ...
    def easing(self) -> QtCore.QEasingCurve: ...
    def method(self) -> 'QMorphingAnimation.Method': ...
    def targetName(self) -> str: ...
    def target(self) -> Qt3DRender.QGeometryRenderer: ...
    def interpolator(self) -> float: ...
    def targetPositions(self) -> typing.List[float]: ...

class QMorphTarget(QtCore.QObject):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    attributeNamesChanged: typing.ClassVar[QtCore.pyqtSignal]
    @staticmethod
    def fromGeometry(geometry: Qt3DCore.QGeometry, attributes: typing.Iterable[str]) -> 'QMorphTarget': ...
    def removeAttribute(self, attribute: Qt3DCore.QAttribute) -> None: ...
    def addAttribute(self, attribute: Qt3DCore.QAttribute) -> None: ...
    def setAttributes(self, attributes: typing.Iterable[Qt3DCore.QAttribute]) -> None: ...
    def attributeNames(self) -> typing.List[str]: ...
    def attributeList(self) -> typing.List[Qt3DCore.QAttribute]: ...

class QSkeletonMapping('QAbstractChannelMapping'):

    def __init__(self, parent: typing.Optional[Qt3DCore.QNode] = ...) -> None: ...

    skeletonChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setSkeleton(self, skeleton: Qt3DCore.QAbstractSkeleton) -> None: ...
    def skeleton(self) -> Qt3DCore.QAbstractSkeleton: ...

class QVertexBlendAnimation('QAbstractAnimation'):

    def __init__(self, parent: typing.Optional[QtCore.QObject] = ...) -> None: ...

    targetNameChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetChanged: typing.ClassVar[QtCore.pyqtSignal]
    interpolatorChanged: typing.ClassVar[QtCore.pyqtSignal]
    targetPositionsChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setTargetName(self, name: str) -> None: ...
    def setTarget(self, target: Qt3DRender.QGeometryRenderer) -> None: ...
    def setTargetPositions(self, targetPositions: typing.Iterable[float]) -> None: ...
    def morphTargetList(self) -> typing.List['QMorphTarget']: ...
    def removeMorphTarget(self, target: 'QMorphTarget') -> None: ...
    def addMorphTarget(self, target: 'QMorphTarget') -> None: ...
    def setMorphTargets(self, targets: typing.Iterable['QMorphTarget']) -> None: ...
    def targetName(self) -> str: ...
    def target(self) -> Qt3DRender.QGeometryRenderer: ...
    def interpolator(self) -> float: ...
    def targetPositions(self) -> typing.List[float]: ...
