import os


def move_file(command):
    list_command = command.split(" ")
    fist_file_name = list_command[1]

    if "/" not in command:

        with open(fist_file_name, "r") as file_in, \
                open(list_command[2], "w") as file_out:
            file_out.write(f"{file_in.read()}")

    else:
        path = "".join(list_command[2])
        list_path = path.split('/')
        second_file_name = "".join(list_path[-1])
        list_path.pop(-1)

        directories = ""
        for directory in list_path:
            directories += f"{directory}/"
            os.mkdir(directories)

        with open(fist_file_name, "r") as file_in, \
                open(second_file_name, "w") as file_out:
            file_out.write(f"{file_in.read()}")

    os.remove(fist_file_name)
