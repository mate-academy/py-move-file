import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return

    mv, first_file, second_file = command
    if mv != "mv":
        return

    dir_path = os.path.dirname(second_file)
    file_name = os.path.basename(second_file)
    file_path = os.path.join(dir_path, file_name) if dir_path else file_name

    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(first_file, "r") as file_in, open(file_path, "w") as file_out:
        file_out.write(file_in.read())

    os.remove(first_file)
