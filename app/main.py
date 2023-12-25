import os


def move_file(command: str) -> None:
    mode, copy, paste = command.split()

    if mode == "mv":
        if "/" in paste:
            os.makedirs(os.path.join(os.getcwd(), os.path.dirname(paste)),
                        exist_ok=True)

        with (open(copy) as from_file,
              open(paste, "w") as to_file):
            to_file.write(from_file.read())
        os.remove(copy)
