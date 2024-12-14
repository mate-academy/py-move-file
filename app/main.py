import os

from contextlib import contextmanager


@contextmanager
def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "mv":
        mv_dir = command_list[-1].split("/")
        with open(command_list[1], "a"):
            pass
        if len(mv_dir) == 1:
            with open(command_list[1],
                      "r") as file_in, open(mv_dir[-1],
                                            "w") as file_out:
                file_out.write(file_in.read())
            os.remove(command_list[1])
        else:
            full_path = ""
            for f_dir in mv_dir[:-1]:
                full_path += f_dir + "/"
                if not os.path.exists(full_path):
                    os.mkdir(full_path)
            with open(command_list[1],
                      "r") as file_in, open(command_list[-1],
                                            "w+") as file_out:
                file_out.write(file_in.read())
            os.remove(command_list[1])
