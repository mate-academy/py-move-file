import os
import shutil


def move_file(command: str) -> None:
    args = command.split(" ")
    if len(args) != 3:
        print("Not enough arguments")
        return
    if args[0] != "mv":
        print("Wrong operation")
        return

    source = args[1]
    target = args[2]

    if os.path.dirname(target) == "":
        perform_move(source, target)
        return

    if target.endswith("/") or target.endswith("\\"):
        target = os.path.join(target, os.path.basename(source))

    perform_move(source, target)

    return


def perform_move(source: str, target: str) -> None:
    dir_name = os.path.dirname(target)
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    shutil.move(source, target)
    return
