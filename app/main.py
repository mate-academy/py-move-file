import os


def move_file(command: str) -> None:
    comm, source, destination = command.split()

    if comm != "mv":
        return

    if destination.endswith("/"):
        file_name = os.path.basename(source)
        final_path = os.path.join(destination, file_name)

    else:
        final_path = destination

    directory = os.path.dirname(final_path)

    if directory:
        directory_list = directory.split("/")
        current_dir = ""
        for direct in directory_list:
            current_dir = os.path.join(current_dir, direct)
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)

    with open(source, "r") as file, open(final_path, "w") as new_file:
        new_file.write(file.read())

    os.remove(source)
