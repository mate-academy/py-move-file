import os


def move_file(command: str) -> None:
    cmd, file_origin, file_new = command.split()
    if (len(command.split()) == 3) and cmd == "mv" and file_origin != file_new:
        directories, file_name = os.path.split(file_new)

        if directories:
            os.makedirs(directories, exist_ok=True)

        new_file_name = os.path.join(directories, file_name)

        with (open(file_origin, "r") as file_in,
              open(new_file_name, "w") as file_out):
            for line in file_in:
                file_out.write(line)

        os.remove(file_origin)
