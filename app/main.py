import os


def move_file(command: str) -> None:
    parts = command.split()

    if (parts[0] == "mv"
       and parts[1] != parts[2]
       and "/" not in parts[2]
       and len(parts) == 3):
        with (open(parts[1], "r") as file_in,
              open(parts[2], "w") as new_file):
            new_file.write(file_in.read())
            file_in.close()
            os.remove(parts[1])

    if (parts[0] == "mv"
       and parts[1] != parts[2]
       and "/" in parts[2]
       and len(parts) == 3):

        current_dir = os.getcwd()

        with open(parts[1], "r") as file_in:

            dirs = parts[2].split("/")
            new_file = dirs.pop(len(dirs) - 1)

            for directory in dirs:
                if os.path.isdir(directory):
                    os.chdir(directory)
                else:
                    os.mkdir(directory)
                    os.chdir(directory)

            with open(new_file, "w") as new_file:
                new_file.write(file_in.read())
                file_in.close()
                os.chdir(current_dir)
                os.remove(parts[1])
