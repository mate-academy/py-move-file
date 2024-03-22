import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) == 3 and command[0] == "mv":
        _, old_file, path_and_new_file = command
        path_and_new_file = path_and_new_file.split("/")
        new_file = path_and_new_file.pop(-1)
        file_path = ""

        for path in path_and_new_file:
            file_path += f"{path}/"
            if not os.path.exists(file_path):
                os.mkdir(file_path)

        with (open(old_file, "r") as from_file,
              open(file_path + new_file, "w") as in_file):
            in_file.write(from_file.read())

        os.remove(old_file)
