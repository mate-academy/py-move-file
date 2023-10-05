import os


def move_file(command: str) -> None:
    commands_list = command.split()
    if len(commands_list) == 3 and commands_list[0] == "mv":
        cmd, file_old, path = commands_list
        directory, file_new = os.path.split(path)
        print(cmd)
        print(file_old)
        print(path)
        if file_old != file_new:
            if directory:
                os.makedirs(directory, exist_ok=True)
            with (open(file_old, "r") as file_in,
                  open(path, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(file_old)
