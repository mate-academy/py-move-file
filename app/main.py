import os


def move_file(command: str) -> None:
    cp_command, current_file, future_file = command.split()
    if cp_command != "mv":
        return
    path_to_file = os.path.split(future_file)
    new_path = ""

    for new_dir in path_to_file[0].split("/"):
        new_path += new_dir + "/"
        if not os.path.exists(new_path):
            os.mkdir(new_path)

    if path_to_file[0] != "":
        with open(
            current_file, "r"
        ) as file, open(
            f"{path_to_file[0]}/{path_to_file[1]}", "w"
        ) as new_file:
            new_file.write(file.read())
        os.remove(current_file)
    else:
        os.rename(current_file, path_to_file[1])
