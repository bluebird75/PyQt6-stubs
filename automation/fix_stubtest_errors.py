from typing import Dict, List, Set, Tuple
import re, pathlib, sys, subprocess

reNameNotDefined = re.compile(r'Name "(.+)" is not defined')

importFixed: Set[Tuple[str, str]] = set()

STUBTEST_COMMAND = [
    sys.executable,
    'automation/stubtest.py', 
    '--allowlist',
     'stubtest.allowlist',
     '--allowlist',
     'stubtest.allowlist.to_review',
     '--allowlist',
     'stubtest.allowlist.windows',
]

BASE_PATH = pathlib.Path(__file__).parent.parent


def fix_stubtest_errors():
    pyqt6_stubs_dir = BASE_PATH / 'PyQt6-stubs'
    for stub_file in pyqt6_stubs_dir.glob('*.pyi'):
        if str(stub_file).startswith("__"):
            print(f"Ignoring file {stub_file}")
            continue

        if stub_file.name != 'QtQuick.pyi':
            continue

        fix_stubtest_errors_for_file(stub_file)
        print('done')


def fix_stubtest_errors_for_file(file_to_fix: pathlib.Path) -> None:
    '''Run stubtest on the stub file and apply some fixes on it.'''
    print('Looking at stubtest results for %s' % file_to_fix.name)
    try:
        call_result = subprocess.run(STUBTEST_COMMAND + ['PyQt6.' + file_to_fix.name[:-4]], cwd=BASE_PATH, text=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE, check=False)
        result = call_result.stdout
    except subprocess.CalledProcessError:
        some_errors = True

    if result.startswith("Success"):
        return

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
            if (file_to_fix.name, nameMissing) in importFixed:
                continue

            for idx, l in enumerate(lines):
                if l.startswith('from PyQt6 import'):
                    lines[idx] = ('from PyQt6 import %s\n' % nameMissing) + lines[idx]
                    importFixed.add((file_to_fix.name, nameMissing))
                    break
            else:
                # we could not find a 'from PyQt6 import' line
                for idx, l in enumerate(lines):
                    if l.startswith('import PyQt6'):
                        lines[idx] = ('from PyQt6 import %s\n' % nameMissing) + lines[idx]
                        importFixed.add((file_to_fix.name, nameMissing))
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


if __name__ == "__main__":
    fix_stubtest_errors()



