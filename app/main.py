import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command.")

    source_path = parts[1]
    destination_path = parts[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file {source_path} does not exist.")

    if destination_path.endswith("/"):
        if os.path.isfile(destination_path):
            raise FileExistsError
        os.makedirs(destination_path, exist_ok=True)
        destination_path = os.path.join(destination_path,
                                        os.path.basename(source_path)
                                        )
    else:
        dir_name = os.path.dirname(destination_path)
        if dir_name:
            if os.path.isfile(dir_name):
                raise FileExistsError
            os.makedirs(dir_name, exist_ok=True)

    # Move (rename) the file
    os.rename(source_path, destination_path)
