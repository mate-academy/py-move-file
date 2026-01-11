import os


def move_file(command: str) -> None:
    file_name = command.split()[1]
    new_path = command.split()[2]
    path_list = new_path.split("/")

    if command.split()[0] == "mv":
        if len(path_list) > 1:
            new_dir = os.path.dirname(new_path)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)

        with (
            open(file_name, "r") as file_out,
            open(new_path, "w") as file_in
        ):
            file_in.write(file_out.read())

            if os.path.exists(file_name):
                os.remove(file_name)
