import os


def move_file(command: str) -> None:
    mv, initial_file, dirs = command.split()
    if mv == "mv":
        path = os.path.dirname(dirs)
        if path:
            os.makedirs(path, exist_ok=True)
        with open(initial_file) as file_in, open(dirs, "w") as file_out:
            file_out.write("".join(file_in.readlines()))
    os.remove(initial_file)
