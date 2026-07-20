import os


def move_file(command: str) -> None:
    mv, source, destination = command.split(" ")
    new_destination = destination.split("/")
    if destination.endswith("/"):
        dirs = new_destination[:-1]
        filename = source.split("/")[-1]
    else:
        dirs = new_destination[: -1]
        filename = new_destination[-1]
    current_path = ""
    for xyz in dirs:
        if current_path == "":
            current_path = current_path + xyz
        else:
            current_path = current_path + "/" + xyz
        if not os.path.exists(current_path):
            os.mkdir(current_path)
    if current_path == "":
        full_destination = filename
    else:
        full_destination = current_path + "/" + filename

    with open(source) as f:
        content = f.read()

    with open(full_destination, "w") as f:
        f.write(content)

    os.remove(source)
