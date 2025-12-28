import os


def move_file(command: str) -> None:
    command, file_out, file_in = command.split()
    path, file_in = os.path.split(file_in)

    if path != "":
        os.makedirs(path, exist_ok=True)

    with open(file_out, "r") as f_out, open(file_in, "w") as f_in:
        f_in.write(f_out.read())
    os.remove(file_out)
