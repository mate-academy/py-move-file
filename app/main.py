import os


def move_file(command: str) -> None:
    new_command = command.split()
    if len(new_command) == 3 and new_command[0] == "mv":
        new_dir = os.path.split(new_command[2])
        if len(new_dir[0]) != 0:
            os.makedirs(new_dir[0], exist_ok=True)
        with (open(new_command[1], "r") as file_in,
              open(new_command[2], "w") as file_out):
            file_out.write(file_in.read())
        os.remove(new_command[1])
