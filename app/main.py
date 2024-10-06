import os


def copying_file(name: str, new_name: str) -> None:
    with (
            open(name, "r") as source,
            open(new_name, "w") as copy_file
    ):
        copy_file.write(source.read())
    os.remove(name)


def move_file(command: str) -> None:
    _command = command.split()
    if len(_command) != 3:
        print("Wrong command!")
        return
    mv, source_file, new_file = _command
    if mv != "mv":
        print('Command should be "mv"')
        return
    *path, file_name = new_file.split("/")

    if not path:
        copying_file(source_file, file_name)
        return

    path = "/".join(path)
    if os.path.exists(path):
        copying_file(source_file, path + "/" + file_name)
    else:
        new_path = os.path.join(path)
        os.makedirs(new_path)
        copying_file(source_file, new_path + "/" + file_name)
