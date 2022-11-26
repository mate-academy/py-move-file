import os


def move_file(command: str) -> None:
    command_list = command.split()
    command_name = command_list[0]
    file_to_remove = command_list[1]
    new_file = command_list[2]

    if command_name == "mv":

        if "/" not in command_list[2] and file_to_remove != new_file:
            os.rename(file_to_remove, new_file)

        else:
            new_file_path = command_list[2].split("/")[:-1]
            creating_path = ""

            for directory in new_file_path:
                os.mkdir(f"{creating_path}{str(directory)}")
                creating_path += str(directory) + "/"

            with open(file_to_remove, "r") as file_out,\
                    open(new_file, "w") as file_in:
                file_in.writelines(file_out.readlines())

            os.remove(file_to_remove)



