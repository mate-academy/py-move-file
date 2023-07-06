import os


def move_file(command: str) -> None:

    command_list = command.split(" ")

    if len(command_list) == 3:
        command_name, src_file, dest_file = command_list

        if command_name == "mv" and os.path.exists(src_file):

            path_dir, new_name = os.path.split(dest_file)
            if path_dir:
                os.makedirs(path_dir, exist_ok=True)

            with (open(src_file, "r") as file_in,
                  open(dest_file, "w") as file_out):
                file_out.write(file_in.read())

            os.remove(src_file)
