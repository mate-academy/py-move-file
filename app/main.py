import os


def move_file(command: str) -> None:
    command_name, source_file_name, destination_file_name = command.split()
    if command_name != "mv":
        return

    if "/" in destination_file_name:
        path_list = destination_file_name.split("/")[:-1]
        check_folder = ""

        for folder in path_list:
            check_folder = os.path.join(check_folder, folder)
            if not os.path.exists(check_folder):
                os.mkdir(check_folder)

        try:
            with (open(source_file_name, "r") as file_in,
                  open(destination_file_name, "w") as file_out):
                content = file_in.read()
                file_out.write(content)

            os.remove(source_file_name)
        except FileNotFoundError:
            return

    else:
        os.rename(source_file_name, destination_file_name)
