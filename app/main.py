import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    instruction = command_list[0]
    in_file_name = command_list[1]
    new_file_destination = command_list[2]
    new_file_path = os.path.dirname(new_file_destination)
    new_file_name = os.path.basename(new_file_destination)
    current_dir = os.getcwd()
    if os.path.exists(in_file_name) and instruction == "mv":
        with open(in_file_name, "r") as in_file:
            file_in = in_file.read()
            if "/" in new_file_destination:
                path_list = new_file_path.split("/")
                for folder in path_list:
                    if not os.path.isdir(folder):
                        os.mkdir(folder)
                    os.chdir(folder)
                with open(new_file_name, "w") as new_file:
                    new_file.write(file_in)
            else:
                with open(new_file_name, "w") as new_file:
                    new_file.write(file_in)

            os.chdir(current_dir)
            in_file.close()
            os.remove(in_file_name)
