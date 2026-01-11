import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return

    action, source_file, destination_file = command.split()
    if action != "mv" or source_file == destination_file:
        return

    if "/" in destination_file:
        (destination_folder,
         destination_file_name) = os.path.split(destination_file)
        if destination_folder:
            os.makedirs(destination_folder)

    else:
        destination_folder = ""
        destination_file_name = destination_file

    with open(source_file, "r") as old_file:
        with open(os.path.join(destination_folder,
                               destination_file_name), "w") as new_file:
            new_file.write(old_file.read())

    os.remove(source_file)
