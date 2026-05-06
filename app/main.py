import os


def move_file(command: str) -> None:
    command = command.split()

    source = command[1]
    path = command[2]

    dirs = os.path.dirname(path)

    parts = dirs.split("/")

    current_path = ""
    if dirs:
        parts = dirs.split("/")
        current_path = ""

        for part in parts:
            current_path += part
            if not os.path.exists(current_path):  # якщо папка не існує
                os.mkdir(current_path)
            current_path += "/"

    with open(source, "r") as file_in, open(path, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(source)
