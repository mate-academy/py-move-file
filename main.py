import os


def move_file(command: str) -> None:
    command, in_file, out_file = command.split()
    if command == "mv":
        path = out_file
        path_list = []
        while path != "":
            path_list.append(os.path.split(path)[1])
            path = os.path.split(path)[0]

        if len(path_list) == 1:
            with (open(in_file, "r")as start_file,
                  open(out_file, "w") as end_file):
                end_file.write(start_file.read())

        else:
            path_list = path_list[3::-1]

            path = ""
            for i in range(len(path_list) - 1):
                if os.path.exists(os.path.join(path, path_list[i])):
                    path = os.path.join(path, path_list[i])
                    print(path)
                else:
                    os.mkdir(os.path.join(path, path_list[i]))
                    path = os.path.join(path, path_list[i])
                    print(path)
            with (open(in_file, "r")as start_file,
                  open(os.path.join(path, path_list[-1]), "w") as end_file):
                end_file.write(start_file.read())

    os.remove(in_file)
