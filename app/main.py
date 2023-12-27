import os


def move_file(command: str) -> None:
    command, in_file, out_file = command.split()
    if command == "mv":
        if "/" in out_file:
            path_list = out_file.split("/")
            path = ""
            for i in range(len(path_list) - 1):
                if os.path.exists(os.path.join(path, path_list[i])):
                    path = os.path.join(path, path_list[i])
                else:
                    os.mkdir(os.path.join(path, path_list[i]))
                    path = os.path.join(path, path_list[i])
            with (open(in_file, "r")as in_f,
                  open(os.path.join(path, path_list[-1]), "w") as out_f):
                out_f.write(in_f.read())
        else:
            with open(in_file, "r")as in_f, open(out_file, "w") as out_f:
                out_f.write(in_f.read())
    os.remove(in_file)
