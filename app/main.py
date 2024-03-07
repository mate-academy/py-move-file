import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]

    try:
        if destination.endswith("/"):
            os.makedirs(destination, exist_ok=True)
            destination_path = os.path.join(destination,
                                            os.path.basename(source))
        else:
            parent_dir = os.path.dirname(destination)
            if parent_dir:
                os.makedirs(parent_dir, exist_ok=True)
            destination_path = destination

        os.replace(source, destination_path)
    except Exception as e:
        print(f"Error moving file: {e}. "
              f"Source: {source}, "
              f"Destination: {destination_path}")
