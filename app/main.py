import os


def move_file(command: str) -> None:
    if not command:
        return
    command_list = command.split()

    if len(command_list) == 3:
        mv, file_name, new_file_name = command_list
        if mv == "mv":
            path_file, name_file = os.path.split(new_file_name)
            if path_file:
                os.makedirs(path_file, exist_ok=True)

            with (open(file_name, "r") as file_in,
                  open(new_file_name, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_name)
