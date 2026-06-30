import os


def move_file(command: str) -> None:
    command_name, source, destination = command.split(" ")

    if command_name != "mv":
        return

    if destination.endswith("/"):
        destination = os.path.join(destination, source)

    directories_path, filename = os.path.split(destination)
    if directories_path:
        directory_list = directories_path.split("/")
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
