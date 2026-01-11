import os


def move_file(command: str) -> None:
    command_str = command.split()

    if len(command_str) != 3 or command_str[0] != "mv":
        raise ValueError
    _, source, target = command_str

    dir_path = os.path.dirname(target).split("/")
    current_path = ""
    if dir_path == [""]:
        dir_path = []

    for dire in dir_path:
        current_path = os.path.join(current_path, dire)
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    if not os.path.isfile(source):
        raise FileNotFoundError(f"{source} does not exist")

    with open(source, "r", encoding="utf-8") as file_in:
        content = file_in.read()

    with open(target, "w", encoding="utf-8") as file_out:
        file_out.write(content)

    os.remove(source)
