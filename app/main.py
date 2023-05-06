import os


def move_file(command: str) -> None:
    content = command.split()
    if "mv" != content[0] or len(content) != 3:
        print("Invalid command. Usage: mv {from_file} {directory}/{to_file}")
        return

    _, move_from, file_path = content
    dirs_to_create, move_to = os.path.split(file_path)

    if move_from == move_to or move_from == file_path:
        print("Cannot create a file when that file already exists")
        return
    elif "/" in dirs_to_create:
        os.makedirs(dirs_to_create, exist_ok=True)

    with open(move_from, "r") as source, open(file_path, "w") as destination:
        destination.write(source.read())
    os.remove(move_from)
