import os


def move_file(command: str) -> None:
    if len(command.split()) != 3 or command[:3] != "mv ":
        return 0
    name_f_in = command.split()[1]
    name_f_out_with_rout = command.split()[2]
    rout_list = name_f_out_with_rout.split("/")
    name_f_out_with_rout_cp = os.path.join(*rout_list)
    os.renames(name_f_in, name_f_out_with_rout_cp)
