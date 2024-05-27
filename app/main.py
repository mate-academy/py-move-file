import os


def move_file(command: str) -> None:
    command, original_file_name, directory = command.split()
    if "/" in directory:
        directory_path = directory.split("/")

        for folder in range(1, len(directory_path)):
            if not os.path.exists("/".join(directory_path[0:folder])):
                os.mkdir("/".join(directory_path[0:folder]))

    with (open(original_file_name, "r") as original_file,
          open(directory, "w") as moved_file):
        moved_file.write(original_file.read())
    os.remove(original_file_name)
