import os


def move_file(command: str) -> None:
    args = command.split()

    if len(args) == 3:
        cmd, file1, file2 = args

        if cmd == "mv" and file1 != file2:
            dir_file2, name_file2 = os.path.split(file2)

            ls_dir_file2 = dir_file2.split("/")
            item = list()
            path_file2 = ""

            for elem in ls_dir_file2:
                item.append(elem)
                path_file2 = os.path.join(*item)

                try:
                    os.makedirs(path_file2, exist_ok=True)
                except WindowsError:
                    continue

            if name_file2 != "":
                path_file2 = os.path.join(path_file2, name_file2)
            else:
                path_file2 = os.path.join(path_file2, file1)

            with (open(file1, "r") as file_in,
                  open(path_file2, "w") as file_out):
                file_out.write(file_in.read())

            os.remove(file1)
