import os


def move_file(command: str) -> None:
    cp_command, current_file, future_file = command.split()
    if cp_command != "mv" or len(command.split()) != 3:
        return
    directories, file_name = os.path.split(future_file)
    new_path = ""

    for new_dir in directories:
        new_path += new_dir
        os.makedirs(new_path, exist_ok=True)

    if directories != "":
        with open(
            current_file, "r"
        ) as file, open(
            f"{directories}/{file_name}", "w"
        ) as new_file:
            new_file.write(file.read())
        os.remove(current_file)
    else:
        os.rename(current_file, file_name)
