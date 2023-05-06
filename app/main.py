import os


def move_file(command: str) -> None:
    content = command.split()
    mv, move_from, file_path = content
    *directory, move_to = file_path.split("/")

    if "mv" != mv or len(content) != 3:
        print("Invalid command. Usage: mv {from_file} {directory}/{to_file}")
        return
    if move_from == move_to or move_from == file_path:
        print("Cannot create a file when that file already exists")
        return

    dirs_path = ""
    for dr in directory:
        dirs_path = os.path.join(dirs_path, dr)
        try:
            os.mkdir(dirs_path)
        except FileExistsError:
            pass

    with open(move_from, "r") as _from, open(file_path, "w") as _to:
        _to.write(_from.read())
    os.remove(move_from)
