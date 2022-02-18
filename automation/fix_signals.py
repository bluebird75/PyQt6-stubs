from typing import Iterable, List, Optional, cast

import pathlib
import importlib
from types import ModuleType

import libcst as cst
from PyQt6 import QtCore, QtDBus

from libcst import MetadataWrapper, parse_module

BASE_PATH = pathlib.Path(__file__).parent.parent

def fix_signals():
    pyqt6_stubs_dir = BASE_PATH / 'PyQt6-stubs'
    for stub_file in pyqt6_stubs_dir.glob('*.pyi'):
        if str(stub_file.name).startswith("__"):
            print(f"Ignoring file {stub_file}")
            continue

        fix_signals_for_file(stub_file)
        print('done')


def fix_signals_for_file(file_to_fix: pathlib.Path) -> None:
    print('Fixing signals for %s' % file_to_fix.name)
    with open(file_to_fix, "r", encoding="utf-8") as fhandle:
        stub_tree = MetadataWrapper(parse_module(fhandle.read()))

    signal_fixer = SignalFixer(file_to_fix.stem)
    modified_tree = stub_tree.visit(signal_fixer)

    with open(file_to_fix, "w", encoding="utf-8") as fhandle:
        fhandle.write(modified_tree.code)



def is_signal(module: ModuleType, cls_name: str, func_name: str) -> bool:
    """Check if a method of the given Qt class is a signal."""
    if cls_name == "QGeoPositionInfoSource" and func_name == "error":
        # this is a fix for the broken error method.
        return False
    try:
        cls = getattr(module, cls_name)
    except AttributeError:
        print(f"Warning! Could not find class {module}.{cls_name}")
        return False
    try:
        func = getattr(cls, func_name)
    except AttributeError:
        print(f"Warning! Could not find method {cls_name}.{func_name}")
        return False
    return isinstance(func, QtCore.pyqtSignal)


class SignalFixer(cst.CSTTransformer):
    """SignalFixer that visits classes and methods to fix signals."""

    def __init__(self, mod_name: str):
        super().__init__()
        self._last_class: List[cst.ClassDef] = []
        self._fixed_signals: List[str] = []
        self._module: ModuleType = importlib.import_module(f"PyQt6.{mod_name}")

    def visit_ClassDef(self, node: cst.ClassDef) -> Optional[bool]:
        """Put a class on top of the stack when visiting."""
        self._last_class.append(node)
        return True

    def leave_FunctionDef(
        self, original_node: cst.FunctionDef, _: cst.FunctionDef
    ) -> cst.BaseStatement | cst.FlattenSentinel[
        cst.BaseStatement
    ] | cst.RemovalSentinel:
        """Leave the method and change signature if a signal."""
        if not self._last_class:
            return original_node
        if len(self._last_class) > 1:
            return original_node

        f_name = original_node.name.value
        if is_signal(self._module, self._last_class[-1].name.value, f_name):
            full_name = f"{self._last_class[-1].name.value}.{f_name}"
            if full_name in self._fixed_signals:
                # Handle the use-case of overloaded signals, that are defined
                # multiple times because of their different signal arguments
                # i.e.: QComboBox.highlighted
                return cst.RemovalSentinel.REMOVE
            self._fixed_signals.append(full_name)
            if self._module.__name__ == "PyQt6.QtCore":
                stmt = f"{f_name}: typing.ClassVar[pyqtSignal]"
            else:
                stmt = f"{f_name}: typing.ClassVar[QtCore.pyqtSignal]"
            node = cst.parse_statement(stmt)
            if original_node.leading_lines:
                # Copy the leading lines and return them with a
                # FlattenSentinel. Just adding a newline char results in an
                # indented EmptyLine which isn't bad but clutters the diff
                # unnecessarily
                empty_nodes = [
                    line.deep_clone() for line in original_node.leading_lines
                ]
                return cst.FlattenSentinel(
                    cast(Iterable[cst.BaseStatement], [*empty_nodes, node])
                )
            return node
        return original_node

    def leave_ClassDef(
        self, original_node: cst.ClassDef, updated_node: cst.ClassDef
    ) -> cst.BaseStatement | cst.FlattenSentinel[
        cst.BaseStatement
    ] | cst.RemovalSentinel:
        """Remove a class from the stack and return the updated node."""
        self._last_class.pop()
        return updated_node


if __name__ == '__main__':
    fix_signals()
