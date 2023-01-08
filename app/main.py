import os


def move_file(command: str) -> None:
    command, file, new_file = command.split()
    if command == "mv":
        full_directory = new_file.split("/")
        new_filename = full_directory[-1]
        with open(file, "r") as old_file:
            reader = old_file.read()
            os.remove(file)
            if len(full_directory) != 1:
                for directory in full_directory[:-1]:
                    if os.path.isdir(directory):
                        os.chdir(directory)
                    else:
                        os.mkdir(directory)
                        os.chdir(directory)
            with open(new_filename, "w") as new_file:
                new_file.write(reader)
