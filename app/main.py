import os


def move_file(command: str) -> None:
    args = command.split()

    if len(args) != 3:
        print("Invalid command format")
        return

    command_name, origin_path, new_path = args

    if not os.path.isfile(origin_path):
        return

    dest_directory = os.path.dirname(new_path)
    if dest_directory:
        os.makedirs(dest_directory, exist_ok=True)

    os.rename(origin_path, new_path)
