import os


def move_file(command: str) -> None:
    command_parts = command.split()
    file_name = command_parts[1]
    new_file_info = command_parts[2]

    if new_file_info.endswith("/"):
        directory_parts = new_file_info.rstrip("/").split("/")
    else:
        directory_parts = new_file_info.split("/")[:-1]

    path = ""
    for part in directory_parts:
        path = os.path.join(path, part)
        if not os.path.exists(path):
            os.mkdir(path)

    if new_file_info.endswith("/"):
        destination = os.path.join(
            new_file_info,
            os.path.basename(file_name),
        )
    else:
        destination = new_file_info

    with open(file_name, "r") as file:
        content = file.read()

    with open(destination, "w") as file:
        file.write(content)
    os.remove(file_name)
