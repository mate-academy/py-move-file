import os


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        cmd, file_old, path = command.split()
        directory, file_new = os.path.split(path)
        if file_old != file_new:
            if directory:
                os.makedirs(directory, exist_ok=True)
            with (open(file_old, "r") as file_in,
                  open(path, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_old)
