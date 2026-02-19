import os


def move_file(command: str) -> None:
    operation = command.split()

    if len(operation) != 3 or operation[0] != "mv":
        return

    __, file_name, description = operation

    try:
        os.makedirs("/".join(description.split("/"))[:-1])
    except FileNotFoundError:
        os.rename(file_name, description)

    with open(file_name, "r") as read, open(description, "w") as write:
        write.write(read.read())

    os.remove(file_name)
