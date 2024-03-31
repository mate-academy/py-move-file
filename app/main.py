import os


def move_file(command: str) -> None:
    move, file_in, file_out = command.split(" ")
    folder_out_path = os.path.dirname(file_out)
    folder_in_path = os.path.dirname(file_in)

    if folder_in_path == folder_out_path:
        os.rename(file_in, file_out)
    else:
        if not os.path.exists(folder_out_path):
            os.makedirs(folder_out_path)

        with (open(file_in, "r") as file_in,
              open(file_out, "w") as file_out):
            file_out.write(file_in.read())
        os.remove(file_in.name)
