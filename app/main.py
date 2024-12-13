import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command format")
        return

    source_path, destination_path = parts[1], parts[2]

    if destination_path.endswith("/"):
        dest_dir = destination_path
        dest_file = os.path.basename(source_path)
    else:
        dest_dir, dest_file = os.path.split(destination_path)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    try:
        os.rename(source_path, os.path.join(dest_dir, dest_file))
    except Exception as e:
        print(f"Error: {e}")
