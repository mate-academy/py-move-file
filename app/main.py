import os


def move_file(command: str) -> None:
    mv_command, from_file, destination_location = command.split()

    if mv_command != "mv":
        raise Exception('Command should start with "mv"!')

    directory_path, to_file = os.path.split(destination_location)
    original_path = os.getcwd()

    if len(directory_path) != 0:
        os.makedirs(directory_path)
        os.chdir(directory_path)

    with open(os.path.join(original_path, from_file), "r") as original, \
            open(to_file, "w") as destination:
        destination.writelines(original)

    os.chdir(original_path)
    os.remove(from_file)
