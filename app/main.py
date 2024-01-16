import os


def move_file(command: str) -> None:
    new_command = command.split()
    if len(new_command) == 3 and new_command[0] == "mv":
        if "/" in new_command[2]:
            new_dir = new_command[2].split("/")
            new_dir.pop(len(new_dir) - 1)  # Delete file name.
            path_of_dir = ""
            for folder in new_dir:  # Create new directory.
                try:
                    path_of_dir += folder + "/"
                    os.mkdir(path_of_dir)
                except FileExistsError:
                    pass
        with (open(new_command[1], "r") as file_in,
              open(new_command[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(new_command[1])
