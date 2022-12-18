import os


def move_file(command: str) -> None:

    sourse = command.split()[1]
    destination = command.split()[2]

    if sourse.endswith("/") or destination.endswith("/"):
        return
    files = destination.split("/")[:-1]

    for direction in files:
        os.mkdir("" + direction)

    with open(sourse, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(sourse)
