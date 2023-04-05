import os


def move_file(command: str) -> None:
    splitted_command = command.split()
    if len(splitted_command) == 3:
        comm, file_name, dir_file = splitted_command
        if comm == "mv":
            directory, new_file = os.path.split(dir_file)
            if os.path.split(dir_file)[0] == "":
                os.rename(file_name, new_file)
            else:
                if not os.path.exists(directory):
                    os.makedirs(directory, exist_ok=True)

                with (open(file_name, "r")
                      as old_file,
                      open(os.path.join(directory, new_file), "w")
                      as new_file):
                    new_file.write(old_file.read())
                os.remove(file_name)
