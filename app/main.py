import os


def move_file(command: str):
    command = command.split()
    command_values = {
        "mode": command[0],
        "file": command[1],
        "file_move": command[2]
    }

    if command_values["mode"] != "mv":
        raise ValueError("You need to use command 'mv' to move file/directory")

    if len(command) != 3:
        raise ValueError("App support only moving of "
                         "files without additional flags")

    file_to_move = command_values["file_move"]
    directory = file_to_move.split("/")
    directory = "/".join(directory[:-1])
    os.makedirs(directory)

    with open(command_values["file"], "r") as f1:
        lines = f1.readlines()
        with open(command_values["file_move"], "w") as f2:
            f2.writelines(lines)

    os.remove(command_values["file"])
