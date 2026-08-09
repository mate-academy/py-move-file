import os


def move_file(command: str) -> None:
    """
    Move a file from one location to another, similar to the Linux
    'mv' command. Creates any missing intermediate directories.

    :param command: str, a command string in the form
        "mv <source_file_name> <destination_path>". If the destination
        path ends with '/', it's treated as a directory and the file
        keeps its original name inside it.
    """
    command_parts = command.split()

    if len(command_parts) != 3 or command_parts[0] != "mv":
        return

    _, source_file_name, destination_path = command_parts

    if destination_path.endswith("/"):
        file_name = os.path.basename(source_file_name)
        destination_path = os.path.join(destination_path, file_name)

    destination_directory = os.path.dirname(destination_path)

    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)

    with open(source_file_name, "r") as source_file, open(
        destination_path, "w"
    ) as destination_file:
        destination_file.write(source_file.read())

    os.remove(source_file_name)
