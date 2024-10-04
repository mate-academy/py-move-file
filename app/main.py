import os


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

    if len(path) == 0:
        with (
            open(source_file, "r") as source,
            open(file_name, "w") as copy_file
        ):
            copy_file.write(source.read())
        os.remove(source_file)
        return

    path = "/".join(path)
    if os.path.exists(path):
        with (
            open(source_file, "r") as source,
            open(path + "/" + file_name, "w") as copy_file
        ):
            copy_file.write(source.read())
    else:
        new_path = os.path.join(path)
        os.makedirs(new_path)
        with (
            open(source_file, "r") as source,
            open(new_path + "/" + file_name, "w") as copy_file
        ):
            copy_file.write(source.read())

    os.remove(source_file)
