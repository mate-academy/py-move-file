import os


def move_file(command: str) -> None:
    command, in_file, out_file, *_ = command.split()
    if command == "mv":
        # path = out_file
        path = os.path.normpath(out_file)
        print(path)

        path = path.split(os.sep)
        print(path)
        *file_path, file_name = path
        print(file_path, file_name)

        if len(file_path) == 0:
            with (open(in_file, "r")as start_file,
                  open(out_file, "w") as end_file):
                end_file.write(start_file.read())

        else:
            path = ""
            for part_of_path in file_path:
                if os.path.exists(os.path.join(path, part_of_path)):
                    path = os.path.join(path, part_of_path)
                else:
                    os.mkdir(os.path.join(path, part_of_path))
                    path = os.path.join(path, part_of_path)
            with (open(in_file, "r") as start_file,
                  open(os.path.join(path, file_name), "w") as end_file):
                end_file.write(start_file.read())

    os.remove(in_file)
