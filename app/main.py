import os


def move_file(command: str) -> None:
    cmd, source_file, destination_path = command.split()

    destination_dir = os.path.dirname(destination_path)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    with open(source_file, "r") as file, open(destination_path, "w") as file2:
        content = file.read()
        file2.write(content)

    os.remove(source_file)
