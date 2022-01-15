import sys
from typing import Union

from PyQt6 import QtCore

OneFlagClass = QtCore.Qt.WindowType

oneFlagRefValue1 = QtCore.Qt.WindowType.Dialog
oneFlagRefValue2 = QtCore.Qt.WindowType.Window

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

	# upcast from OneFlagClass to int
	intValue = oneFlagValue1

	# conversion also accepted
	intValue = int(oneFlagValue1)

	# this is not supported type-safely for a good reason
	oneFlagValueTest = 1		# type: ignore

	# correct way to do it
	oneFlagValueTest = OneFlagClass(1)
	oneFlagValueTest = OneFlagClass(oneFlagValue1)

	assert_type_of_value_oneFlag(oneFlagValue1 | oneFlagValue2)
	assert_type_of_value_oneFlag(oneFlagValue1 & oneFlagValue2)
	assert_type_of_value_oneFlag(oneFlagValue1 ^ oneFlagValue2)
	assert_type_of_value_oneFlag(~oneFlagValue1)
	assert_type_of_value_int(oneFlagValue1 + oneFlagValue2)
	assert_type_of_value_int(oneFlagValue1 - oneFlagValue2)
	assert_type_of_value_int(oneFlagValue1 * oneFlagValue2)
	assert_type_of_value_int(oneFlagValue1 // oneFlagValue2)

	assert_type_of_value_oneFlag(oneFlagValue1 | 1)
	assert_type_of_value_oneFlag(oneFlagValue1 & 1)
	assert_type_of_value_oneFlag(oneFlagValue1 ^ 1)
	assert_type_of_value_int(oneFlagValue1 + 1)
	assert_type_of_value_int(oneFlagValue1 - 1)
	assert_type_of_value_int(oneFlagValue1 * 1)
	assert_type_of_value_int(oneFlagValue1 // 1)

	assert_type_of_value_oneFlag(1 | oneFlagValue1)
	assert_type_of_value_oneFlag(1 & oneFlagValue1)
	assert_type_of_value_oneFlag(1 ^ oneFlagValue1)
	assert_type_of_value_int(1 + oneFlagValue1)
	assert_type_of_value_int(1 - oneFlagValue1)
	assert_type_of_value_int(1 * oneFlagValue1)
	assert_type_of_value_int(1 // oneFlagValue1)



	oneFlagValueTest = OneFlagClass(oneFlagValue1)
	assert_type_of_value_oneFlag(oneFlagValueTest)

	# this is rejected for the same reason as for OneFlagClass.
	intValue = oneFlagValueTest

	# correct way to do it
	intValue = int(oneFlagValueTest)
	assert_type_of_value_int(intValue)

	# rejected by mypy rightfully
	oneFlagValueTest = 1            # type: ignore

	# correct way to do it
	oneFlagValueTest = OneFlagClass(1)

	oneFlagValueTest = oneFlagValue1  # reset type and value
	assert_type_of_value_oneFlag(oneFlagValueTest)
	oneFlagValueTest |= oneFlagValue2
	assert_type_of_value_oneFlag(oneFlagValueTest)   # nice violation of Liskov principle here

	oneFlagValueTest = oneFlagValue1  # reset type and value
	assert_type_of_value_oneFlag(oneFlagValueTest)
	oneFlagValueTest |= 1
	assert_type_of_value_oneFlag(oneFlagValueTest)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue &= oneFlagValue2
	assert_type_of_value_oneFlag(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue &= 1
	assert_type_of_value_oneFlag(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue ^= oneFlagValue2
	assert_type_of_value_oneFlag(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue ^= 1
	assert_type_of_value_oneFlag(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue += oneFlagValue2
	assert_type_of_value_int(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue -= oneFlagValue2
	assert_type_of_value_int(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue *= oneFlagValue2
	assert_type_of_value_int(oneFlagOrIntValue)

	oneFlagOrIntValue = oneFlagValue1	# reset type and value
	assert_type_of_value_oneFlag(oneFlagOrIntValue)
	oneFlagOrIntValue //= oneFlagValue2
	assert_type_of_value_int(oneFlagOrIntValue)

	assert_type_of_value_oneFlag(oneFlagValue1 & ~oneFlagValue2)

