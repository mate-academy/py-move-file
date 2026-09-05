from os import mkdir, remove, path


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError
    _, old_file, new_file = parts
    if new_file[-1] == "/":
        new_file += old_file
    file_path = new_file.split("/")
    current_path = ""
    for i in range(len(file_path) - 1):
        try:
            mkdir(path.join(current_path, file_path[i]))
        except FileExistsError:
            continue
        finally:
            current_path = path.join(current_path, file_path[i])
    with (open(old_file, "r")) as old, (open(new_file, "w")) as new:
        new.write(old.read())
    remove(old_file)
