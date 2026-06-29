import os


def move_file(command: str) -> None:
    command_in_list = command.split(" ")
    if len(command_in_list) != 3 or command_in_list[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Expected: 'mv <source> <destination>'")
    old_file = command_in_list[1]
    destination_path = command_in_list[-1]
    if destination_path.endswith("/") or destination_path.endswith("\\"):
        dir_path = destination_path
        new_file = os.path.basename(old_file)
    else:
        dir_path = os.path.dirname(destination_path)
        new_file = os.path.basename(destination_path)
    if dir_path:
        normalized_dir = os.path.normpath(dir_path)
        parts = normalized_dir.split(os.sep)
        current_path = ""
        for part in parts:
            if not part:
                continue
            current_path = os.path.join(current_path, part) \
                if current_path else part
            if not os.path.exists(current_path):
                os.mkdir(current_path)
    if dir_path:
        full_path = os.path.join(os.path.normpath(dir_path), new_file)
    else:
        full_path = new_file
    with open(old_file, "r") as source_file:
        content = source_file.read()
    with open(full_path, "w") as destination_file:
        destination_file.write(content)
    os.remove(old_file)
