import os


def move_file(command: str) -> None:
    tokens = command.split(" ")
    required_command = tokens[0]
    if required_command == "mv" and len(tokens) == 3:
        filename = tokens[1]
        if "/" in tokens[2]:
            path = tokens[2].split("/")
            is_file = "." in path[-1]
            dir_parts = path[:-1] if is_file else path
            current = ""
            for part in dir_parts:
                current = os.path.join(current, part)
                try:
                    os.mkdir(current)
                except FileExistsError:
                    pass

            if is_file:
                file_path = os.path.join(*path)
                with open(file_path, "w") as new_file, \
                        open(filename, "r") as old_file:
                    data = old_file.read()
                    new_file.write(data)
                os.remove(filename)
        else:
            new_filename = tokens[2]
            with open(filename, "r") as old_filename, \
                    open(new_filename, "w") as f:
                data = old_filename.read()
                f.write(data)
            os.remove(filename)
