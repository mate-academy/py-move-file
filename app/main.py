import os


def move_file(command: str) -> None | str:

    if len(command.split()) != 3:
        return "Incorrect statement printed"

    cmd, curent_file, destination = command.split()

    if cmd != "mv":
        return "Command is incorrect"

    dir_list = destination.split("/")
    new_file_name = dir_list[-1]
    dir_list.remove(new_file_name)

    try:
        os.makedirs("/".join(dir_list))
    except FileExistsError:
        print("Folder is already exists")
    except FileNotFoundError:
        print("Not need to create folders")

    with open(curent_file, "r") as source_file, open(destination, "w") as moved_file:
        moved_file.write(source_file.read())
    os.remove(curent_file)
