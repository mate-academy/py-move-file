import os


def move_file(command: str) -> None:
    _, source_file, destination_path = command.split()
    if not os.path.dirname(destination_path):
        destination_file = destination_path
        os.rename(source_file, destination_file)
    elif destination_path.endswith("/"):
        os.makedirs(destination_path, exist_ok=True)
        destination_file = os.path.join(destination_path,
                                        os.path.basename(source_file))
        os.rename(source_file, destination_file)
    else:
        destination_file = destination_path
        destination_path = os.path.dirname(destination_path)
        os.makedirs(destination_path, exist_ok=True)
        os.rename(source_file, destination_file)
