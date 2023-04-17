import os


def move_file(line: str) -> None:
    command_line = line.split()
    if len(command_line) == 3:
        command, file, directory_file = command_line
        if command == "mv":
            folders_and_file = directory_file.split("/")
            if len(folders_and_file) == 1:
                os.replace(file, directory_file)
            else:
                folders = "/".join(folders_and_file[:-1])
                new_file = folders_and_file[-1]
                if not os.path.isdir(folders):
                    os.makedirs(folders)
                os.replace(file, folders + "/" + new_file)
