import os


def move_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "mv":
        return

    source = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))

    split_dis = destination.split("/")
    dirs = split_dis[:-1]

    current_path = ""
    for directory in dirs:
        current_path = os.path.join(current_path, directory)
        if not os.path.isdir(current_path):
            os.mkdir(current_path)

    with open(source, "r") as file_in:
        content = file_in.read()

    with open(destination, "w") as file_out:
        file_out.write(content)

    os.remove(source)
