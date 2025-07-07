import os


def move_file(mv_command: str) -> None:

    file_list = mv_command.strip().split()

    if len(file_list) == 3 and file_list[0] == "mv":
        src = file_list[1]
        dest = file_list[2]

        with open(src, "r") as file_in:
            content = file_in.read()

        paths = dest.split("/")[:-1]
        current_path = ""

        for path in paths:
            current_path += path
            try:
                os.mkdir(current_path)
            except FileExistsError:
                current_path += "/"
            else:
                current_path += "/"

        with open(dest, "w") as file_out:
            file_out.write(content)

        os.remove(file_list[1])
