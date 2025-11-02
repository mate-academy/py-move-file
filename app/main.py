from os import remove, mkdir, path


def move_file(command: str) -> None | list:
    command_parts = command.split(" ")
    if command_parts[0] == "mv" and len(command_parts) == 3:
        file_in = command_parts[1]
        file_out = command_parts[2]
        if file_in != file_out:
            if "/" in file_out:
                full_path = file_out.split("/")[0:-1]
                directory = ""
                for catalogue in full_path:
                    directory += catalogue
                    if not path.exists(directory):
                        mkdir(directory)
                    directory += "/"
            try:
                with (
                    open(file_in) as source_file,
                    open(file_out, "w") as target_file
                ):
                    target_file.write(source_file.read())
                    remove(file_in)
            except FileNotFoundError:
                pass
