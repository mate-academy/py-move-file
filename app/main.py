import os


def move_file(command: str) -> None:
    elements = command.split()
    if len(elements) == 3:
        command, file_in, file_path = elements
        if command == "mv":
            path = os.path.dirname(file_path)
            if len(path) > 1:
                os.makedirs(path, exist_ok=True)
            with open(file_in, "r") as f_in, open(file_path, "w") as f_out:
                f_out.write(f_in.read())
            os.remove(file_in)
