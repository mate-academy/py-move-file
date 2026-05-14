import os


def move_file(command: str) -> None:

    command_parts = command.split()
    if len(command_parts) != 3:
        return

    mv, file_name, destination_path = command_parts
    if mv != "mv":
        return
    path_parts = destination_path.split("/")

    new_file = path_parts[-1]
    directory = path_parts[:-1]

    if directory:
        for index, dir_names in enumerate(directory):
            current_path = os.path.join(*directory[:index + 1])
            if not os.path.exists(current_path):
                os.mkdir(current_path)
        path_new_file = os.path.join(current_path, new_file)
        with (
            open(file_name, "r") as file_in,
            open(path_new_file, "w") as file_out
        ):
            read_content = file_in.read()
            file_out.write(read_content)
        os.remove(file_name)
    else:
        with open(file_name, "r") as file_in, open(new_file, "w") as file_out:
            read_content = file_in.read()
            file_out.write(read_content)
        os.remove(file_name)
