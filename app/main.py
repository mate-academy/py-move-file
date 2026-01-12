from pathlib import Path
import shutil


def move_file(command: str) -> None:
    print("command: ", command)
    if not isinstance(command, str):
        return

    command_arr = command.split()

    if len(command_arr) != 3:
        return

    cv_command = command_arr[0]
    name_file = command_arr[1]
    path_for_move = command_arr[2]

    if cv_command != "mv":
        return

    if path_for_move[-1] == "/":
        path_for_move += name_file

    source = Path(name_file)
    destination = Path(path_for_move)

    if not source.exists() or not source.is_file():
        return

    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
    except FileExistsError:
        return
    except Exception:
        return

    shutil.move(str(source), str(destination))
