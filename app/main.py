import os


def move_file(command: str) -> None:
    command = command.split()
    if (len(command) == 3):
        cmd, file_origin, file_new = command

        if cmd == "mv" and file_new != file_origin:

            directories, file_name = os.path.split(file_new)
            if directories:
                os.makedirs(directories, exist_ok=True)

            with (open(file_origin, "r") as file_in,
                  open(file_new, "w") as file_out):
                file_out.write(file_in.read())

            os.remove(file_origin)
