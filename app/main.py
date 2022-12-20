import os


def move_file(command: str) -> None:
    mv_command, from_file, destination_location = command.split()

    if mv_command != "mv":
        raise Exception('Command should start with "mv"!')

    *directories, to_file = destination_location.split("/")
    directory_path = ""

    for directory in directories:
        directory_path = os.path.join(directory_path, directory)
        os.mkdir(directory_path)

    with open(from_file, "r") as original, \
            open(os.path.join(directory_path, to_file), "w") as destination:
        destination.writelines(original)

    os.remove(os.path.join(from_file))
