import sys
from typing import Union

from PyQt6 import QtCore

OneFlagClass = QtCore.Qt.WindowState

oneFlagRefValue1 = QtCore.Qt.WindowState.WindowMinimized
oneFlagRefValue2 = QtCore.Qt.WindowState.WindowMaximized

def assert_type_of_value_int(value: int) -> None:
	'''Raise an exception if the value is not of type expected_type'''
	assert type(value) == int

def assert_type_of_value_oneFlag(value: OneFlagClass) -> None:
	'''Raise an exception if the value is not of type expected_type'''
	assert type(value) == OneFlagClass


def test_on_one_flag_class() -> None:
	oneFlagValue1 = oneFlagRefValue1
	oneFlagValue2 = oneFlagRefValue2
	oneFlagValueTest: OneFlagClass
	intValue: int
	oneFlagOrIntValue: Union[int, OneFlagClass]

	# this is not supported type-safely for a good reason
	oneFlagValueTest = 1		# type: ignore

	# correct way to do it
	oneFlagValueTest = OneFlagClass(1)
	oneFlagValueTest = OneFlagClass(oneFlagValue1)

	assert_type_of_value_oneFlag(oneFlagValue1 | oneFlagValue2)
	assert_type_of_value_oneFlag(oneFlagValue1 & oneFlagValue2)
	assert_type_of_value_oneFlag(oneFlagValue1 ^ oneFlagValue2)
	assert_type_of_value_oneFlag(~oneFlagValue1)				# type: ignore


	oneFlagValueTest = OneFlagClass(oneFlagValue1)
	assert_type_of_value_oneFlag(oneFlagValueTest)

	# correct way to do it
	oneFlagValueTest = OneFlagClass(1)

	oneFlagValueTest = oneFlagValue1  # reset type and value
	assert_type_of_value_oneFlag(oneFlagValueTest)
	oneFlagValueTest |= oneFlagValue2
	assert_type_of_value_oneFlag(oneFlagValueTest)   # nice violation of Liskov principle here

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue &= oneFlagValue2
	assert_type_of_value_oneFlag(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue ^= oneFlagValue2
	assert_type_of_value_oneFlag(oneFlagOrIntValue)

	assert_type_of_value_oneFlag(oneFlagValue1 & ~oneFlagValue2)

