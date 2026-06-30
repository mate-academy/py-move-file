import os


def move_file(command: str) -> None:
    command_items = command.split(" ")
    if len(command_items) != 3 or command_items[0] != "mv":
        return
    command_name, source, destination = command_items


    if destination.endswith(os.path.sep):
        destination = os.path.join(destination, source)

    directories_path, filename = os.path.split(destination)

    if directories_path:
        directory_list = []
        while directories_path:
            directories_path, tail = os.path.split(directories_path)
            if tail:
                directory_list.append(tail)
            else:
                if directories_path:
                    directory_list.append(directories_path)
                    break

        directory_list.reverse()

        path = ""
        for directory in directory_list:
            path = os.path.join(path, directory)
            if not os.path.exists(path):
                os.mkdir(path)

    with (
        open(source, "r") as source_file_object,
        open(destination, "w") as destination_file_object
    ):
        destination_file_object.write(source_file_object.read())

    os.remove(source)
