import os


def move_file(command: str) -> None:
    command_parts = command.split()
    file_old = command_parts[1]
    if "/" in command_parts[2]:
        directories_list = command_parts[2].split("/")
        file_new = directories_list[-1]
        directories_list = directories_list[0:-1]
        directories = "/".join(directories_list)
        directories += "/"
        os.makedirs(directories)
        with open(file_old, "r") as file_in, open(file_new, "w") as file_out:
            file_out.write(file_in.read())
            file_in.close()
            os.remove(f"{file_in}")
            os.replace(f"{file_out}", f"{command_parts[2]}")
    else:
        file_new = command_parts[2]
        with open(file_old, "r") as file_in, open(file_new, "w") as file_out:
            file_out.write(file_in.read())
            file_in.close()
            os.remove(f"{file_in}")
