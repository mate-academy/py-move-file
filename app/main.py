from os import mkdir, remove, path, rename


def move_file(command: str) -> None:
    try:
        mv, file, new_location = command.split()
        if mv != "mv":
            raise ValueError
    except ValueError:
        raise ValueError(
            "Incorrect command. Example: mv file1.txt file2.txt "
            "or mv file1.txt new_folder/file1.txt"
        )

    if "/" not in new_location and file != new_location:
        rename(file, new_location)

    elif "/" in new_location:
        directories, new_file = new_location.rsplit("/", 1)
        full_path = ""
        for directory in directories.split("/"):
            full_path = path.join(full_path, directory)
            if not path.exists(full_path):
                mkdir(full_path)

        with open(file) as read_file, open(new_location, "w") as write_file:
            write_file.write(read_file.read())
        remove(file)
