import os


def move_file(command: str) -> None:
    args = command.split(" ")

    if len(args) == 3:
        cmd, file1, file2 = args

        if cmd == "mv" and file1 != file2:
            dir_path = file2.split("/")
            path = ""

            for elem in dir_path:
                if "." not in elem:
                    path += elem + "/"

                    try:
                        os.mkdir(path)
                        print(path)
                    except WindowsError:
                        continue
                elif "." in elem:
                    with (open(file1, "r") as file_in,
                            open(file2, "w") as file_out):
                        file_out.write(file_in.read())
                else:
                    with (open(file1, "r") as file_in,
                            open(file1, "w") as file_out):
                        file_out.write(file_in.read())

            os.remove(file1)
