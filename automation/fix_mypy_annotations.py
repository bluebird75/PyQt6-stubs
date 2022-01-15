from typing import Dict, List, Set, Tuple
from collections import defaultdict
import os, re
from mypy import api as mypy_api

reNameNotDefined = re.compile(r'Name "(.+)" is not defined')

importFixed: Set[Tuple[str, str]] = set()

def prepare_files() -> Dict[str, List[int]]:
    """Preprare the files and apply some quick fixes."""
    # Apply the quick fixes from mypy:
    annotations: Dict[str, List[int]] = defaultdict(list)

    for stub_file in os.listdir("PyQt6-stubs"):
    # for stub_file in ['Qt3DAnimation.pyi']:
        if stub_file.startswith("__"):
            print(f"Ignoring file {stub_file}")
            continue

        file_to_fix = os.path.join("PyQt6-stubs", stub_file)

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

                fix_done = True
                for idx, l in enumerate(lines):
                    if l.startswith('from PyQt6 import'):
                        lines[idx] = ('from PyQt6 import %s\n' % nameMissing) + lines[idx]
                        importFixed.add((stub_file, nameMissing))
                        break
            elif error_msg == 'Overload does not consistently use the "@staticmethod" decorator on all function signatures.':
                fix_done = True
                lines[line_nbr - 1] = lines[line_nbr - 1][:-1] + "  # type: ignore[misc]\n"
            elif "Signature of" in error_msg and "incompatible with supertype" in error_msg:
                fix_done = True
                lines[line_nbr - 1] = lines[line_nbr - 1][:-1] + "  # type: ignore[override]\n"
            elif " is incompatible with supertype " in error_msg or " incompatible with return type " in error_msg:
                fix_done = True
                lines[line_nbr - 1] = lines[line_nbr - 1][:-1] + "  # type: ignore[override]\n"
            elif " will never be matched: signature " in error_msg:
                fix_done = True
                annotations[stub_file.replace(".pyi", "")].append(line_nbr)

            print('Fixing: ' + line)

        with open(file_to_fix, "w", encoding="utf-8") as w_handle:
            w_handle.writelines(lines)

    return annotations

if __name__ == "__main__":
    prepare_files()



