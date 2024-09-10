import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    cmd, source_file_name, destination_path = command_list
    destination_dir = os.path.dirname(destination_path)

    if cmd != "mv" or len(command_list) < 2:
        return

    if not os.path.exists(destination_dir) and "/" in destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    if source_file_name != destination_path:
        with (open(source_file_name, "r") as file_in,
              open(destination_path, "w") as file_out):
            content = file_in.read()
            file_out.write(content)

        os.remove(source_file_name)
