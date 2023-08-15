import os


def move_file(command: str) -> None:
    command_list = command.split()

    command_name = command_list[0]
    file_1_name = command_list[1]
    file_2_path = command_list[2]

    file_2_name = file_2_path.split("/")[-1]
    dirs = file_2_path.split("/")[:-1]

    if command_name == "mv":
        with open(file_1_name, "r") as file_1:
            default_dir = os.getcwd()

            for directory in dirs:

                if not os.path.isdir(directory):
                    os.mkdir(directory)
                os.chdir(directory)

            with open(file_2_name, "w") as file_2:
                file_2.write(file_1.read())

        os.chdir(default_dir)
        os.remove(file_1_name)
