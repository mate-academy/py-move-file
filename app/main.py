import os.path


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, from_path, to_path = command.split()
        if command_name == "mv":
            with open(from_path, "r") as from_file:
                source_data = from_file.read()
                path_part = to_path.split("/")
                full_path = ""
                for path in path_part:
                    full_path = os.path.join(full_path, path)
                    if path.count(".") != 0:
                        with open(full_path, "w") as to_file:
                            to_file.write(source_data)
                            break
                    if not os.path.exists(full_path):
                        os.mkdir(full_path)
            os.remove(from_file.name)
