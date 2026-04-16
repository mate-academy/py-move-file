import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) == 3 and command_parts[0].lower() == "mv":
        source_path = command_parts[1]
        dest_path = command_parts[2]

        is_dir = dest_path.endswith(("/", "\\", os.path.sep))

        filename = os.path.basename(source_path)

        if is_dir:
            dir_path = dest_path
            final_dest_path = os.path.join(dir_path, filename)
        else:
            final_dest_path = dest_path
            dir_path = os.path.dirname(dest_path)

        if dir_path:
            clean_dir_path = os.path.normpath(dir_path)
            folders = clean_dir_path.split(os.sep)

            current_path = ""
            for folder in folders:
                if folder:
                    if current_path:
                        current_path = os.path.join(current_path, folder)
                    else:
                        current_path = folder

                    if not os.path.exists(current_path):
                        os.mkdir(current_path)

        with (
            open(source_path, "r") as f_source,
            open(final_dest_path, "w") as f_dest
        ):
            f_dest.write(f_source.read())

        os.remove(source_path)
