import os


def move_file(command: str) -> None:
    copy_command, name, path = command.split()
    if "/" not in path:
        with open(name, "r") as file_in, open(path, "w") as file_out:
            file_out.write(file_in.read())
            os.remove(name)

    dir_names = ""
    for word in path.split("/")[:-1]:
        dir_names += word + "/"
        os.mkdir(dir_names)

    new_path = dir_names + path.split("/")[-1]

    if path.endswith("/"):
        new_path = dir_names + name

    with open(name, "r") as file_in, open(new_path, "w") as file_out:
        file_out.write(file_in.read())
        os.remove(name)
