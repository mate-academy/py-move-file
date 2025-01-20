import os


def move_file(command: str) -> None:
    if not command.startswith("mv"):
        return

    command_split = command.split()
    if len(command_split) != 3:
        return

    _, filename_in, filename_out = command_split

    if filename_out.find("/") != -1:
        dirs_with_filename = filename_out.split("/")
        dirs_path = "/".join(dirs_with_filename[:len(dirs_with_filename) - 1])
        os.makedirs(dirs_path, exist_ok=True)

        if filename_out.endswith("/"):
            filename_out += filename_in

    with (open(filename_in, "r") as file_in,
          open(filename_out, "w") as file_out):
        file_out.writelines(file_in.read())
        os.remove(filename_in)
