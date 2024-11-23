import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if command_parts[0] == "mv" and len(command_parts) == 3:
        mv_command, file_name, file_path = command_parts
        path_parts = file_path.split("/")
        current_dir = path_parts[0]
        if len(path_parts) == 1:
            os.rename(file_name, file_path)
            return
        elif len(path_parts) == 2:
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)
        else:
            if not os.path.exists(current_dir):
                os.mkdir(current_dir)
            for next_path_part in path_parts[1:-1]:
                current_dir = os.path.join(current_dir, next_path_part)
                if not os.path.exists(current_dir):
                    os.mkdir(current_dir)

        with open(file_name) as source_file:
            source_file_content = source_file.read()
        final_file_path = os.path.join(current_dir, path_parts[-1])
        with open(final_file_path, "w") as destination_file:
            destination_file.write(source_file_content)
            os.remove(file_name)
