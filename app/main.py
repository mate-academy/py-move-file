import os


def move_file(command: str) -> None:
    command, original_file_name, directory = command.split()
    if "/" in directory:
        directory_path = directory.split("/")
        os.makedirs("/".join(directory_path[:-1]), exist_ok=True)

    with (open(original_file_name, "r") as original_file,
          open(directory, "w") as moved_file):
        moved_file.write(original_file.read())
    os.remove(original_file_name)
