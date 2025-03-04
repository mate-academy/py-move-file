import os


def move_file(move_command: str) -> None:

    command_list = move_command.split()
    if len(command_list) != 3:
        print("Incorrect input info")
        return
    file_command, file_source, file_target = command_list

    if file_command != "mv":
        print("Incorrect command")
        return
    with open(file_source, "r") as f_source:
        create_directory(file_target)
        with open(file_target, "w") as f_target:
            for line in f_source:
                f_target.write(line)
    os.remove(file_source)
    try:
        open(file_source, "r")
    except FileNotFoundError:
        print(f"File {file_source} successfully deleted.")


def create_directory(full_path: str) -> None:
    path_parts = full_path.split("/")
    if len(path_parts) < 2:
        return

    path_seek = ""
    for i in range(len(path_parts) - 1):
        # path_seek += path_parts[i] + "/"
        path_seek = os.path.join(path_seek, path_parts[i])
        if not os.path.isdir(path_seek):
            os.mkdir(path_seek)
