import os


def move_file(command: str) -> None:

    command_name, file_to_remove, new_file = command.split()

    if command_name == "mv":

        if "/" not in new_file and file_to_remove != new_file:
            os.rename(file_to_remove, new_file)

        else:
            new_file_directories = new_file.split("/")[:-1]
            creating_path = "/".join(new_file_directories)
            os.makedirs(creating_path)
            new_file_path = "/".join(new_file.split("/"))

            with open(file_to_remove, "r") as file_out,\
                    open(new_file_path, "w") as file_in:
                file_in.writelines(file_out.readlines())

            os.remove(file_to_remove)