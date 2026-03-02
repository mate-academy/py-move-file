import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "mv":
        raise ValueError(
            "Invalid command format! Use: mv <source_file> <destination_path>"
        )

    _, source_file, destination_file = command

    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"File {source_file} does not exist!")

    destination_file_dir = os.path.dirname(destination_file)
    if destination_file_dir:
        os.makedirs(destination_file_dir, exist_ok=True)

    with open(source_file, "r") as src_file:
        with open(destination_file, "w") as dst_file:
            dst_file.write(src_file.read())

    os.remove(source_file)
