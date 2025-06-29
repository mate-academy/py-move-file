import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if command_parts[0] != "mv":
        return

    if command_parts[1] == command_parts[2]:
        return

    file_content = ""

    try:
        with open(command_parts[1], "r") as file:
            file_content = file.read()
    except FileNotFoundError:
        return
    directories = command_parts[2].split("/")[:-1]
    if directories:
        current_path = directories[0]
        if not os.path.exists(current_path):
            os.mkdir(current_path)

        for directory in directories[1:]:
            current_path = os.path.join(current_path, directory)
            if not os.path.exists(current_path):
                os.mkdir(current_path)

    with open(command_parts[2], "w") as file:
        file.write(file_content)

    os.remove(command_parts[1])
