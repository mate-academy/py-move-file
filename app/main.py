import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) != 3 or command_list[0] != "mv":
        return

    _, moved_file, destination_list = (command_list[0],
                                       command_list[1],
                                       command_list[2].split("/"))

    if destination_list[-1].find(".") == -1:
        destination_list.append(moved_file)

    path = ""

    for destination in range(len(destination_list) - 1):
        # path += destination_list[destination] + "/"
        path = os.path.join(path, destination_list[destination])
        os.makedirs(path, exist_ok=True)
    if path:
        path += "/"
    with (
        open(path + destination_list[-1], "w") as file_rename,
        open(moved_file) as file_reader
    ):
        file_rename.write(file_reader.read())

    os.remove(moved_file)
