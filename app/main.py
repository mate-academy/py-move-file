import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    command_split = command.split()
    command_name = command_split[0]
    file_cp = command_split[1]
    file_path = command_split[2]
    if command_name == "mv":
        if file_path[-1] == "/":
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with (open(file_cp, "r") as f,
                  open(f"{file_path}/{file_cp}", "w") as f_cp):
                for line in f:
                    f_cp.write(line)
            os.remove(file_cp)
            return
        if len(file_path.split("/")) == 1:
            root, ext_f = os.path.splitext(file_path)
            root1, ext_cp = os.path.splitext(file_path)
            if ext_f == ext_cp:
                os.rename(file_cp, file_path)
            return
        file_path_split = file_path.split("/")
        cp_file_txt = file_path_split.pop(-1)
        file_path = "/".join(file_path_split)
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        with (open(file_cp, "r") as f,
              open(f"{file_path}/{cp_file_txt}", "w") as f_cp):
            for line in f:
                f_cp.write(line)
        os.remove(file_cp)
    return
