import os


def move_file(command: str) -> None:
    command_line_split = command.split()
    if command_line_split[0] == "mv":
        direction_path = command_line_split[2].split("/")[:-1]
        new_path = ""
        for directory in direction_path:
            os.mkdir(f"{new_path}{str(directory)}")
            new_path += str(directory) + "/"
        with open(f"{command_line_split[1]}", "r") as file_in,\
                open(f"{command_line_split[2]}", "w") as file_out:
            file_out.write(file_in.read())
        os.remove(command_line_split[1])
