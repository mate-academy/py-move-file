import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) < 3:
        return
    if command[0] != "mv":
        return

    com = command[2].split("/")
    folder = com[:-1]
    file_name = com[-1]
    path = ""
    for i in folder:
        path += i + "/"
        if not os.path.exists(path):
            os.mkdir(path)
    path += file_name

    with (open(command[1], "r") as
          file_in, open(path, "w") as file_out):
        file_out.write(file_in.read())
    os.remove(command[1])
