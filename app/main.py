from os import makedirs, remove, path


def move_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        mv_command, file_in_name, file_out_path = command_list
        if mv_command == "mv" and file_in_name != file_out_path:
            file_out_path = path.normpath(file_out_path)
            file_out_dir = path.dirname(file_out_path)
            if file_out_dir:
                makedirs(file_out_dir, exist_ok=True)
            with (open(file_in_name, "r") as file_in,
                  open(file_out_path, "w") as file_out):
                file_out.write(file_in.read())
            remove(file_in_name)
