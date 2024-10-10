import os


def move_file(command: str) -> None:
    split_command = command.split()
    mv, file_1, path_file_2 = split_command

    if "/" in command:
        path = path_file_2[0:path_file_2.rfind("/")]

        if not os.path.exists(path):
            os.makedirs(path)
        with (open(file_1, "r") as file_in,
              open(path_file_2, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(file_1)
    else:
        if not os.path.exists(path_file_2):
            with (open(file_1, "r") as file_in,
                  open(path_file_2, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_1)
        else:
            os.rename(file_1, path_file_2)
