import os
import shutil


def move_file(command: str) -> None:
    try:
        assert len(command.split()) == 3, "Command should have 3 arguments"
        assert command.split()[0] == "mv", "First command should be 'mv'"
    except AssertionError as e:
        print(e)
        return

    order, old_file, new_location = command.split()
    if os.path.sep in new_location:
        directories = os.path.split(new_location)[0]
        os.makedirs(directories, exist_ok=True)

    try:
        shutil.move(old_file, new_location)
    except Exception as exc:
        print(exc)
