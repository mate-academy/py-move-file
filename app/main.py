import os


def move_file(command: str) -> None:
    cp_command, current_file, future_file = command.split()

    path_to_file = future_file.split("/")[:-1]
    new_path = ""

    for new_dir in path_to_file:
        new_path += new_dir + "/"
        if not os.path.exists(new_path):
            os.mkdir(new_path)

    with open(
            f"{current_file}", "r"
    ) as file, open(
        f"{future_file}", "w"
    ) as new_file:
        new_file.write(file.read())
    os.remove(current_file)
