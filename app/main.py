import os


def move_file(command: str) -> None:
    cmd, source_file, destination_path = command.split()

    with open(source_file, "r") as file:
        content = file.read()

    destination_dir = os.path.dirname(destination_path)

    os.makedirs(destination_dir, exist_ok=True)

    with open(destination_path, "w") as file2:
        file2.write(content)

    os.remove(source_file)
