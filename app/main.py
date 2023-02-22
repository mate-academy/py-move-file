from os import makedirs, remove


def move_file(command: str) -> None:
    mv_command, file, new_location = command.split()
    if mv_command != "mv":
        raise ValueError(
            "Incorrect command. Example: mv file1.txt file2.txt "
            "or mv file1.txt new_folder/file1.txt"
        )

    if "/" in new_location:
        makedirs(new_location.rsplit("/", 1)[0])

    with open(file) as read_file, open(new_location, "w") as write_file:
        write_file.write(read_file.read())
    remove(file)
