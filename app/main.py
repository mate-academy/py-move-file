import os


def move_file(command: str) -> None:
    try:
        act, source, path = command.split()
    except ValueError:
        return

    dirs = os.path.dirname(path)

    current_path = ""

    if dirs and act == "mv":
        parts = dirs.split("/")
        current_path = ""

        for part in parts:
            current_path = os.path.join(current_path, part)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(source, "r") as file_in, open(path, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
