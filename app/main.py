import os


def move_file(command: str) -> None:
    if command[:2] == "mv":
        names = command.split()
        if len(names) == 3:
            # inside len(names) == 3
            if "/" in names[2]:

                os.makedirs(os.path.dirname(names[2]), exist_ok=True)

            # still inside len(names) == 3
            os.rename(names[1], names[2])
