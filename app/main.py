import os


def move_file(command):
    list_command = command.split(" ")
    fist_file_name = list_command[1]
    with open(fist_file_name, "r") as file_in, \
            open("new_file.txt", "w") as file_out:
        file_out.write(f"{file_in.read()}")
    if "/" not in command:
        os.rename(fist_file_name, list_command[2])
    else:
        path = "".join(list_command[2])
        list_path = path.split('/')
        second_file_name = "".join(list_path[-1])
        list_path.pop(-1)
        directories = ""
        for directory in list_path:
            directories += f"{directory}/"
            os.mkdir(directories)
        with open("new_file.txt", "r") as file_in, \
                open(second_file_name, "w") as file_out:
            file_out.write(f"{file_in.read()}")
        os.remove("new_file.txt")
