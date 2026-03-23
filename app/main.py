import os


def move_file(command: str) -> None:
    if not command.strip():
        return None
    parts = command.strip().split()
    if len(parts) != 3:
        return None
    if parts[0] != "mv":
        return None

    file_in_name = parts[1]
    file_out_name = parts[2]

    if file_in_name == file_out_name:
        return None
    if os.path.isdir(file_out_name) or file_out_name.endswith("/"):
        file_out_name = os.path.join(file_out_name, file_in_name)
    # check are there a name of file

    dir_path = os.path.dirname(file_out_name)
    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    try:
        with open(file_in_name, "r") as file_in:  # save a files data
            data = file_in.read()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"[Errno2] No such file or directory: {file_in_name}"
        )
    # writing in a file block
    with open(file_out_name, "w") as file_out:
        file_out.write(data)
    os.remove(file_in_name)
