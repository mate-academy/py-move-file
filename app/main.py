import os


def move_file(command: str) -> None:
    if command.strip() == "":
        return

    command_token = command.split()

    if command_token[0] != "mv":
        return

    if len(command_token) != 3:
        return

    source = command_token[1]
    destination = command_token[2]

    if "/" not in destination:
        os.rename(source, destination)
        return

    if os.path.isdir(destination) or destination.endswith("/"):
        file_name = os.path.basename(source)
        dir_path = destination
    else:
        file_name = os.path.basename(destination)
        dir_path = os.path.dirname(destination)

    with open(source, "rb") as source_file:
        copycat = source_file.read()

    dir_path = os.path.normpath(dir_path)
    os.makedirs(dir_path, exist_ok=True)

    target = os.path.join(dir_path, file_name)

    if os.path.exists(target):
        raise FileExistsError(f"Target file '{target}' already exists")

    with open(target, "wb") as file:
        file.write(copycat)
    os.remove(source)
