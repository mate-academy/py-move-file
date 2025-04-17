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

    if target == os.path.basename(target):
        os.rename(source, target)
        return

    if target.endswith("/") or target.endswith("\\"):
        target = os.path.join(target, os.path.basename(source))
        perform_move(source, target)
        return

    perform_move(source, target)

    return


def perform_move(source: str, target: str) -> None:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    shutil.move(source, target)
    return
