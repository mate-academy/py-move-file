import os


def move_file(command: str) -> None:
    command, file_name_in, file_name_out, *_ = command.strip().split()
    path_dir = os.path.dirname(file_name_out)

    if path_dir and not os.path.exists(path_dir):
        os.makedirs(path_dir, exist_ok=True)

    with (open(file_name_in, "r") as file_in,
          open(f"{file_name_out}", "w+") as file_out):
        file_out.write(file_in.read())
    os.remove(file_name_in)
