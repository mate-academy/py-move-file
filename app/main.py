import os


def move_file(command: str) -> None:
    list_from_command = command.split(" ")
    if len(list_from_command) != 3:
        return
    if list_from_command[0] != "mv":
        return
    if list_from_command[1] == list_from_command[2]:
        return
    if "/" not in list_from_command[2]:
        os.rename(list_from_command[1], list_from_command[2])
        return
    directories = list_from_command[2].split("/")
    path = ""
    for folder in directories[:-1]:
        path = os.path.join(path, folder)
        os.mkdir(path)
    with open(list_from_command[1], "r") as file_in, open(
        list_from_command[2], "w"
    ) as file_out:
        file_out.write(file_in.read())
    os.remove(list_from_command[1])
