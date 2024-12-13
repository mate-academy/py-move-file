import os


class SourceFileNotFoundError(Exception):
    pass


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use 'mv source_file destination_file'.")

    source_file = os.path.abspath(parts[1])
    destination_file = os.path.abspath(parts[2])

    # Check if the source file exists
    if not os.path.exists(source_file):
        raise SourceFileNotFoundError(f"Source file '{source_file}' "
                                      f"not found.")

    # Ensure the destination directory exists
    destination_dir = os.path.dirname(destination_file)
    os.makedirs(destination_dir, exist_ok=True)

    # Move the file to the destination
    os.replace(source_file, destination_file)
