from os import makedirs, remove, path


def move_file(command: str):

    current_file_name, directory_and_new_name = command.split(" ")[1:]

    if "/" in directory_and_new_name:
        directory, new_name = directory_and_new_name.rsplit("/", 1)
        makedirs(directory)
    else:
        new_name = directory_and_new_name
        directory = ""

    with open(current_file_name, "r") as input_file, \
            open(path.join(directory, new_name), "w") as output_file:
        output_file.write(input_file.read())
        remove(current_file_name)
