import os


def move_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] == "mv" and len(command_list) == 3:
        if "/" in command_list[2]:
            path_parts = command_list[2].split("/")
            path_to_file = ""
            for part in path_parts:
                path_to_file = os.path.join(path_to_file, part)
                if not os.path.exists(path_to_file):
                    os.mkdir(path_to_file)
            with open(command_list[1], "r") as file_in,\
                    open(path_to_file, "w") as file_out:
                file_out.write(file_in.read())
            os.remove(command_list[1])

        else:
            os.rename(command_list[1], command_list[2])
