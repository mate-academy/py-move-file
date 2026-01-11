import os


def move_file(command: str) -> None:
    moving_file, path = command.split()[1:]
    new_path = "/".join(path.split("/")[0:-1])
    if len(new_path) > 0:
        os.makedirs(new_path, exist_ok=True)

    with open(moving_file, "r") as file, open(path, "w") as new_file:
        new_file.write(file.read())
    os.remove(moving_file)
