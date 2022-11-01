import os


def move_file(command: str) -> None:
    list_command = command.split(" ")

    first_filename = list_command[1]

    mv_file_path = list_command[2].split("/")

    second_filename = ""
    for name in mv_file_path:
        if ".txt" in name:
            second_filename += name

    new = "/".join(mv_file_path[:-1])

    if not os.path.exists(new):
        os.makedirs(new)

    new_file_path = f"{new}/{second_filename}"

    os.rename(first_filename, new_file_path)
