import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "mv":
        if parts[1] == parts[2]:
            return
        directory, _ = os.path.split(parts[2])
        if len(directory) != 0:
            os.makedirs(directory, exist_ok=True)
        with (open(parts[1], "r") as file_in,
              open(parts[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(parts[1])
