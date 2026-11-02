import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) < 3:
        return

    command, file_in, file_out = command[0], command[1], command[2]

    if command != "mv":
        return

    path = file_out.split("/")
    directory = ""

    if len(path) == 1:
        os.rename(file_in, file_out)
        return

    for folder in path[:-1]:
        directory = os.path.join(directory, folder)
        if not os.path.exists(directory):
            os.mkdir(directory)

    with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
        f_out.write(f_in.read())

    os.remove(file_in)
