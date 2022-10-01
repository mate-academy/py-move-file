from os import makedirs, remove


def move_file(command: str):
    command_parts = command.split()
    source_file = command_parts[1]
    second_file_path = command_parts[2]
    destination_folder = second_file_path.rsplit("/", 1)[0]
    makedirs(destination_folder)

    with open(source_file, "r") as file:
        source_data = file.read()

    with open(second_file_path, "w") as copied_file:
        copied_file.write(source_data)

    remove(source_file)
