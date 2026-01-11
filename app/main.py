import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    if parts[0] != "mv" or len(parts) != 3:
        raise ValueError("Invalid command format.")

    if not os.path.exists(parts[1]):
        raise FileNotFoundError("No such file.")

    file_path = parts[2].split("/")

    if len(file_path) > 1:
        directory = file_path[0]
        for name in file_path[1:]:
            if not os.path.exists(directory):
                os.mkdir(directory)
            directory += "/" + name

    with open(parts[1], "r") as old_file, open(parts[2], "w") as new_file:
        new_file.write(old_file.read())
        old_file.close()
        os.remove(parts[1])
