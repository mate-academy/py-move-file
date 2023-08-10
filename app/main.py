import os


def move_file(command: str) -> None:

    if len(command.split()) == 3:
        action, file_name, path = command.split()
        if action == "mv":
            with open(file_name) as file_to_read:
                if "/" in path:
                    list_of_directories = path.split("/")[:-1]
                    file_name_to_move = path.split("/")[-1]
                    current_path = os.getcwd()
                    for folder in list_of_directories:
                        current_path = os.path.join(current_path, folder)
                        if not os.path.isdir(current_path):
                            os.mkdir(current_path)

                    with (open(os.path.join(current_path,
                                            file_name_to_move), "w")
                          as file_to_write):
                        file_to_write.write(file_to_read.read())

                else:
                    with open(path, "w") as file_to_write:
                        file_to_write.write(file_to_read.read())
            os.remove(file_name)
