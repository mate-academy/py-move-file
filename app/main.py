import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use 'mv source destination'.")

    source_path = command_parts[1]
    destination_path = command_parts[2]

    is_directory = destination_path.endswith("/")

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"'{source_path}' not found.")

    if is_directory:
        os.makedirs(destination_path, exist_ok=True)

    if is_directory:
        destination_path = os.path.join(destination_path,
                                        os.path.basename(source_path))

    os.rename(source_path, destination_path)
