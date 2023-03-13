import os


def move_file(command: str) -> None:
    command_list = command.split(" ")
    instruction = command_list[0]
    in_file_name = command_list[1]
    new_file_name = command_list[2]
    current_dir = os.getcwd()
    if os.path.exists(in_file_name):
        with open(in_file_name, "r") as in_file:
            if instruction == "mv":
                if "/" in new_file_name:
                    path_list = new_file_name.split("/")
                    for i, folder in enumerate(path_list):
                        if i < len(path_list) - 1:
                            if not os.path.isdir(folder):
                                os.mkdir(folder)
                                os.chdir(folder)
                            else:
                                os.chdir(folder)
                        else:
                            with open(folder, "w") as new_file:
                                file_in = in_file.read()
                                new_file.write(file_in)
                                os.chdir(current_dir)
                                in_file.close()
                                os.remove(in_file_name)

                else:
                    with open(new_file_name, "w") as new_file:
                        file_in = in_file.read()
                        new_file.write(file_in)
                        in_file.close()
                        os.remove(in_file_name)
