import os


def move_file(command: str) -> None:
    command, file_in, file_out_with_rout = command.split()
    if command == "mv":
        rout_list = file_out_with_rout.split("/")
        file_out_with_rout_cp = os.path.join(*rout_list)
        os.renames(file_in, file_out_with_rout_cp)
