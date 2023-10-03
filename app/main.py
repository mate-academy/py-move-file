import os


def move_file(command: str) -> None:
    separate = command.split()
    if len(separate) == 3:
        cmd, part_1, part_2 = separate
        if cmd == "mv":
            if "/" in part_2:
                directory_way, new_file = os.path.split(part_2)
                os.makedirs(directory_way, exist_ok=True)
                with (open(part_1, "r") as old_file,
                     open(part_2, "w") as new_file):
                    new_file.write(old_file.read())
                os.remove(part_1)
            else:
                os.rename(part_1, part_2)
