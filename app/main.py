from os import makedirs, remove, path


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or command_split[0] != "mv":
        print("Invalid  usage. mv <file> <directory/file_moved>")
        return

    command_name, filename, moved_file_path = command_split

    directories = moved_file_path.split("/")

    moved_file = directories.pop()

    folder_path = ""
    for i in range(len(directories)):
        folder_path = path.join(folder_path, directories[i])
        makedirs(folder_path, exist_ok=True)

    if folder_path != "":
        moved_file = path.join(folder_path, moved_file)

    with (
        open(filename, "r") as source,
        open(moved_file, "w") as new_file
    ):
        new_file.write(source.read())

    remove(filename)
