import os


def move_file(command: str) -> None:
    command, file, directory = command.split()
    if command == "mv":
        if "/" in directory:
            command_ls = directory.split("/")
        else:
            command_ls = directory
        for direction in command_ls[:-1]:
            file_directory = directory[: directory.index(direction)]
            os.mkdir(f"{file_directory}{direction}")

        with open(file, "r") as first_file, open(directory, "w") as copy:
            copy.write(first_file.read())

        os.remove(file)
