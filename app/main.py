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
            new_file_directories = command_list[2].split("/")[:-1]
            creating_path = "/".join(new_file_directories)
            os.makedirs(creating_path)
            new_file_path = "/".join(command_list[2].split("/"))

            with open(file_to_remove, "r") as file_out,\
                    open(new_file_path, "w") as file_in:
                file_in.writelines(file_out.readlines())

            os.remove(file_to_remove)
