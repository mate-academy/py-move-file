import os


def move_file(command: str) -> None:
    _, source_file_name, destination_file_name = command.split()

    destination_dir = os.path.dirname(destination_file_name)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(source_file_name, "r") as source_file_object, \
            open(destination_file_name, "w") as destination_file_object:
        destination_file_object.write(source_file_object.read())

    os.remove(source_file_name)
