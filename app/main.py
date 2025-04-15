import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) != 3:
        return

    mv, first_file, second_file = command
    if mv != "mv":
        return

    second_file = second_file.split("/")
    if len(second_file) == 1:
        with (open(first_file, "r") as file_in,
              open("".join(second_file), "w") as file_out):
            file_out.write(file_in.read())
        os.remove(first_file)
        return

    dir_path = "/".join(second_file[:-1])
    file_path = os.path.join(dir_path, second_file[-1])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(first_file, "r") as file_in, open(file_path, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(first_file)
