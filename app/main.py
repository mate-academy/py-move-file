import os
import shutil


def move_file(command: str) -> None:
    try:
        order, old_file, new_location = command.split()
        assert order == "mv", "First command should be 'mv'"
    except (AssertionError, ValueError) as e:
        print(e)
        return

    if os.path.sep in new_location:
        directories = os.path.split(new_location)[0]
        os.makedirs(directories, exist_ok=True)

    try:
        shutil.move(old_file, new_location)
    except Exception as exc:
        print(exc)
