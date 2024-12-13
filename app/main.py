import os


def move_file(command: str) -> None:
    command_ls = command.split(" ")

    if len(command_ls) == 3:
        prefix = command_ls[0]
        file_name = command_ls[1]
        file_path = command_ls[2]

        if prefix == "mv" and file_name != file_path:
            dir_path = ""
            dir_ls = file_path.split("/")

            for i in range(len(dir_ls) - 1):
                if dir_path:
                    dir_path += "/" + dir_ls[i]
                else:
                    dir_path += dir_ls[i]
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)

            with (
                open(file_name, "r") as file_in,
                open(file_path, "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(file_name)
