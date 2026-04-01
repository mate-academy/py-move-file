import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Command must contain exactly three parts: 'mv',"
                         " 'file_name', and 'directory'")

    cm, name_file, directory = parts

    if cm != "mv":
        raise ValueError("The first part of the command must be 'mv'")
    if name_file == directory or directory == "":
        raise ValueError("The file name and directory"
                         " cannot be the same or empty")

    new_dir = os.path.dirname(directory)
    if new_dir:
        os.makedirs(new_dir, exist_ok=True)

    with open(name_file, "r") as old_file, open(directory, "w") as new_file:
        new_file.write(old_file.read())

    os.remove(name_file)
