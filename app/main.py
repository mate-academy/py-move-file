import os.path


def move_file(command: str) -> None:
    source_command = command.split()

    if len(source_command) == 3 and source_command[0] == "mv":
        mv, file_name, new_file_name = source_command

        if "/" in new_file_name:
            way, name_file = os.path.split(new_file_name)
            os.makedirs(way, exist_ok=True)

            with (open(file_name, "r") as file_1,
                  open(new_file_name, "w") as file_2,
                  ):
                file_2.write(file_1.read())
            os.remove(file_name)
        else:
            os.rename(file_name, new_file_name)
