import os


def move_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "mv":
        raise ValueError("Something wrong. "
                         "Command example: "
                         "'mv source destination'")

    source = command_list[1]
    dest = command_list[2]

    if not os.path.isfile(source):
        raise FileNotFoundError(f"File {source} not found.")

    if dest.endswith("/"):
        os.makedirs(dest, exist_ok=True)
        dest = os.path.join(dest, os.path.basename(source))
    else:
        dest_dir = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)

    os.rename(source, dest)
