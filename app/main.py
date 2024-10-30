import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3:
        command_name, source_filepath, target_filepath = command_split

        if command_name == "mv" and source_filepath != target_filepath:
            if target_filepath.endswith("/"):
                os.makedirs(target_filepath, exist_ok=True)
            else:
                target_dir = os.path.dirname(target_filepath)
                if target_dir and not os.path.exists(target_dir):
                    os.makedirs(target_dir, exist_ok=True)
            with (open(source_filepath, "r") as file_in,
                  open(target_filepath, "w") as file_out):
                file_out.write(file_in.read())
            os.remove(source_filepath)
