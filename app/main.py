import os


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) != 3 or commands[0] != "mv":
        return

    source = commands[1]
    destinations = commands[2].split("/")

    if source == commands[2]:
        return

    current_path = []
    for destination in destinations[:-1]:
        current_path.append(destination)
        path = os.path.join(*current_path)

        if os.path.isdir(path):
            continue

        os.mkdir(path)

    if commands[2].endswith("/"):
        full_path = os.path.join(
            *current_path,
            os.path.basename(source)
        )
    else:
        full_path = os.path.join(*current_path, destinations[-1])

    with open(source, "r") as file, open(full_path, "w") as file_write:
        content = file.read()
        file_write.write(content)

    os.remove(source)
