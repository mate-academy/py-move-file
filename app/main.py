import os


def move_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] != "mv":
        print("Please enter the right command")
        return
    if "/" in command_list[2]:
        path_list = command_list[2].split("/")
    if "\\" in command_list[2]:
        path_list = command_list[2].split("\\")
    path = ""
    for i in range(len(path_list) - 1):
        path = os.path.join(path, path_list[i])
        os.mkdir(path)
    with (open(command_list[1], "r") as source,
          open(command_list[2], "w") as moved):
        moved.write(source.read())
    os.remove(command_list[1])
