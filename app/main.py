import os


def move_file(command: str) -> None:
    command_split = command.split()
    command_name, filename, moved_file_path = command_split
    directories = moved_file_path.split("/")
    moved_file = directories.pop()

    folder_path = ""
    for i in range(len(directories)):
        folder_path = os.path.join(folder_path, directories[i])
        os.makedirs(folder_path, exist_ok=True)

    if folder_path != "":
        moved_file = os.path.join(folder_path, moved_file)

    with (
        open(filename, "r") as source,
        open(moved_file, "w") as new_file
    ):
        new_file.write(source.read())

    os.remove(filename)
