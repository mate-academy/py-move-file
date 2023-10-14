import os


def move_file(command: str) -> None:
    if not command:
        return
    command_list = command.split()
    if command_list[0] == "mv" and len(command_list) == 3:
        if "/" in command_list[2]:
            path_file = command_list[2].split("/")
            os.makedirs("/".join(path_file[:-1]), exist_ok=True)

        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(command_list[1])
