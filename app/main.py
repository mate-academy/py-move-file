import os


def move_file(command: str) -> None:
    mv, file_in, file_out = command.split(" ")
    if mv != "mv":
        return
    os.makedirs("/".join(file_out.split("/")[:-1]))
    if file_out.split("/")[-1] == "":
        raise FileNotFoundError
    with open(file_in, "r") as source, \
            open(file_out, "w") as new_file:
        new_file.write(source.read())
    os.remove(file_in)
