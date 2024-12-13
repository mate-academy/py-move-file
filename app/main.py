from os import makedirs, remove, path


def move_file(full_command: str) -> None:
    command, file_name, directory = full_command.split()
    if command != "mv":
        return

    new_directory, file_name_out = path.split(directory)
    makedirs(new_directory)
    full_directory_with_name = new_directory + "/" + file_name_out

    with (
        open(file_name, "r") as file_in,
        open(full_directory_with_name, "w") as file_out
    ):
        file_out.write(file_in.read())
        remove(file_name)
