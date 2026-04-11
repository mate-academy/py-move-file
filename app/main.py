import os


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        if "/" in command_list[2]:
            if os.path.isdir(command_list[2]):
                raise FileExistsError
            directory = os.path.dirname(command_list[2])
            os.makedirs(directory, exist_ok=True)
        with open(command_list[1], "r") as file_in, \
                open(command_list[2], "w") as file_out:
            file_out.write(file_in.read())
        os.remove(command_list[1])
