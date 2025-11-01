import os


def move_file(command: str) -> None:
    args = command.split()

    if len(args) != 3 or args[0] != "mv" or args[1] == args[2]:
        return

    source_path = args[1]
    destination_path = args[2]

    with open(source_path, "r") as from_file:
        data = from_file.read()

    path, file_name = os.path.split(destination_path)
    if path != "":
        os.makedirs(path, exist_ok=True)

    if file_name == "":
        file_name = os.path.basename(source_path)

    full_path = os.path.join(path, file_name)
    with open(full_path, "w") as to_file:
        to_file.write(data)

    os.remove(source_path)
