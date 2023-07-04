import os


def move_file(command: str) -> None:

    command_name, src_file, dest_file = command.split(" ")

    if command_name == "mv" and os.path.exists(src_file):

        dest_list = dest_file.split("/")
        path_dir = ""

        for new_dir in dest_list[:-1]:
            path_dir = os.path.join(path_dir, new_dir)
            if not os.path.exists(path_dir):
                os.mkdir(path_dir)

        with (open(src_file, "r") as file_in,
              open(dest_file, "w") as file_out):
            file_out.write(file_in.read())

        os.remove(src_file)
