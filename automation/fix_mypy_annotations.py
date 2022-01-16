from typing import Dict, List, Set, Tuple
from collections import defaultdict
import os, re, pathlib
from mypy import api as mypy_api

reNameNotDefined = re.compile(r'Name "(.+)" is not defined')

importFixed: Set[Tuple[str, str]] = set()

def prepare_files() -> Dict[str, List[int]]:
    """Preprare the files and apply some quick fixes."""
    # Apply the quick fixes from mypy:
    annotations: Dict[str, List[int]] = defaultdict(list)

    for stub_file in os.listdir("PyQt6-stubs"):
        if stub_file.startswith("__"):
            print(f"Ignoring file {stub_file}")
            continue

        pyqt6_stubs_dir = pathlib.Path(__file__).parent.parent / 'PyQt6-stubs'
        file_to_fix = os.path.join(pyqt6_stubs_dir, stub_file)

        result = mypy_api.run([file_to_fix])[0]
        if result.startswith("Success"):
            continue

        with open(file_to_fix, "r", encoding="utf-8") as handle:
            lines = handle.readlines()

        for line in result.split("\n"):
            fix_done = False
            try:
                line_nbr = int(line.split(":", 2)[1])
            except IndexError:
                # Ignore first line ("Found x errors[...]" and empty last line.
                continue
            try:
                error_msg = line.split("error: ")[1]
            except IndexError:
                # Do no parse stuff like notes...
                continue

            mo = reNameNotDefined.match(error_msg)
            if mo:
                nameMissing = mo.group(1)
                if '.' in nameMissing:
                    # this is a sub-import, don't fix it blindly
                    continue
                if (stub_file, nameMissing) in importFixed:
                    continue

                for idx, l in enumerate(lines):
                    if l.startswith('from PyQt6 import'):
                        lines[idx] = ('from PyQt6 import %s\n' % nameMissing) + lines[idx]
                        importFixed.add((stub_file, nameMissing))
                        break
                else:
                    # we could not find a 'from PyQt6 import' line
                    for idx, l in enumerate(lines):
                        if l.startswith('import PyQt6'):
                            lines[idx] = ('from PyQt6 import %s\n' % nameMissing) + lines[idx]
                            importFixed.add((stub_file, nameMissing))
                            break
                    else:
                        # not fixed...
                        continue

                fix_done = True
            elif error_msg == 'Overload does not consistently use the "@staticmethod" decorator on all function signatures.':
                lines[line_nbr - 1] = lines[line_nbr - 1][:-1] + "  # type: ignore[misc]\n"
                fix_done = True
            elif "Signature of" in error_msg and "incompatible with supertype" in error_msg:
                lines[line_nbr - 1] = lines[line_nbr - 1][:-1] + "  # type: ignore[override]\n"
                fix_done = True
            elif " is incompatible with supertype " in error_msg or " incompatible with return type " in error_msg:
                lines[line_nbr - 1] = lines[line_nbr - 1][:-1] + "  # type: ignore[override]\n"
                fix_done = True
            elif 'Unused "type: ignore" comment' in error_msg:
                codeline = lines[line_nbr - 1]
                codeline = codeline[:codeline.index('#')]+'\n'
                lines[line_nbr - 1] = codeline
                fix_done = True
            elif "Overloaded function signature" in error_msg and\
                    "will never be matched: signature" in error_msg and \
                    "parameter type(s) are the same or broader" in error_msg:
                lines[line_nbr - 1] = lines[line_nbr - 1][:-1] + "  # type: ignore[misc]\n"
                fix_done = True

            if fix_done:
                print('Fixing: ' + line)

        with open(file_to_fix, "w", encoding="utf-8") as w_handle:
            w_handle.writelines(lines)

    return annotations

if __name__ == "__main__":
    prepare_files()



