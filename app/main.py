from os import mkdir, remove


def move_file(command: str) -> None:
    if command.startswith("mv "):
        if "/" in command:
            file_name = command.split()[1]
            paths = command.split()[2]
            command = ""
            for directory in paths.split("/"):
                command += directory
                if "." not in command:
                    try:
                        mkdir(command)
                    except FileExistsError:
                        pass

                command += "/"

            with (open(file_name, "r") as file_to_copy,
                  open(paths, "w") as file_copy):
                file_copy.write(file_to_copy.read())
            remove(file_name)
        else:
            file_name = command.split()[1]
            final_name = command.split()[2]
            with (open(file_name, "r") as file_to_copy,
                  open(final_name, "w") as file_copy):
                file_copy.write(file_to_copy.read())
            remove(file_name)
