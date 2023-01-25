import os
import pathlib


def move_file(command: str) -> None:
    splitted = command.split()
    if len(splitted) == 3:
        cmd, source, target = splitted
        if cmd != "mv":
            return
        if "/" not in target:
            with (
                open(source, "r") as source_file,
                open(target, "w") as target_file
            ):
                target_file.write(source_file.read())
        else:
            target = target.split("/")
            path = str(pathlib.Path().absolute()) + "/"
            target_file = target[-1]
            for i in range(len(target) - 1):
                path += target[i] + "/"
            target = os.path.join(path, target_file)
            os.makedirs(path)
            with (
                open(source, "r") as source_file,
                open(target, "w") as target_file
            ):
                target_file.write(source_file.read())

        os.remove(source)
