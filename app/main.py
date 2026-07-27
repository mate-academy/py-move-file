import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return
    command_name, file_to_move, path = parts

    if command_name != "mv":
        return

    home_dir = os.getcwd()
    content = ""

    with open(file_to_move, "r") as src:
        content = src.read()

    folder_path = os.path.dirname(path)
    file_name = os.path.basename(path)

    full_path = os.path.join(folder_path, file_name)

    if folder_path and not os.path.isdir(folder_path):
        os.makedirs(folder_path, exist_ok=True)

    with open(full_path, "w") as f:
        f.write(content)

    os.chdir(home_dir)
    os.remove(os.path.join(home_dir, file_to_move))
