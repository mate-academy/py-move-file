import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    move_cmd, source_path_str, dest_path_str = parts

    try:
        with open(source_path_str, "r") as source_file:
            content = source_file.read()
    except FileNotFoundError:
        return

    if dest_path_str.endswith("/"):
        dest_path_str += os.path.basename(source_path_str)

    current_path = ""
    directories = dest_path_str.split("/")
    for directory in directories[:-1]:
        current_path += f"{directory}/"
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(dest_path_str, "w") as dest_file:
        dest_file.write(content)

    os.remove(source_path_str)
