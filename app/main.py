import os


def move_file(command: str) -> None:
    command_split = command.split()
    if command_split[0] == "mv":
        new_path = ""
        directory = command_split[2].split("/")[:-1]
        for direct in directory:
            os.mkdir(f"{new_path}{str(direct)}")
            new_path += str(direct) + "/"
        with open(f"{command_split[1]}", "r") as file_in, \
                open(f"{command_split[2]}", "w") as file_out:
            file_out.write(file_in.read())
        os.remove(command_split[1])
