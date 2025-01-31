import os


def move_file(command: str) -> None:
    if len(command.split()) == 3 and command.split()[0] == "mv":
        _, old_file, new_file = command.split()
        dir_path, new_file_name = os.path.split(new_file)

        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

        with open(old_file, "r") as in_file, open(new_file, "w") as out_file:
            out_file.write(in_file.read())

        os.remove(old_file)
