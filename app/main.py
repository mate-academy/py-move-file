import os


def move_file(command: str) -> None:
    if not command:
        return
    command_list = command.split()

    if len(command_list) == 3:
        mv, file_name, new_file_name = command_list
        if mv == "mv":
            if "/" in new_file_name:
                path_file = new_file_name.split("/")
                os.makedirs("/".join(path_file[:-1]), exist_ok=True)

            with (open(file_name, "r") as file_in,
                  open(new_file_name, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_name)
