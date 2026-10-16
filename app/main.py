import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "mv":
        return
    source = parts[1]
    destination = parts[2]
    destination = destination.split("/")
    directory = destination[:-1]
    path = ""
    for directory in directory:
        path = os.path.join(path, directory)
        if not os.path.exists(path):
            os.mkdir(path)
    if destination[-1] == "":
        destination[-1] = os.path.basename(source)
    full_path = os.path.join(path, destination[-1])
    with open(source, "r") as file_in, open(full_path, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
    os.remove(source)
