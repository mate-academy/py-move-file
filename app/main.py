import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) < 3:
        print("Not enough arguments")
        return
    cd, source_name, target_name, *_ = command_parts
    if cd != "mv":
        return

    if "/" in target_name:
        *target_path_parts, file_name = target_name.split("/")
        current_path = ""
        for directory in target_path_parts:
            current_path = os.path.join(
                current_path, directory
            ) if current_path else directory
            try:
                os.mkdir(current_path)
            except FileExistsError:
                pass

        target_name = os.path.join(current_path, file_name)
    try:
        with open(source_name, "rb") as source_file:
            with open(target_name, "wb") as target_file:
                target_file.write(source_file.read())

        os.remove(source_name)

    except FileNotFoundError:
        print(f"File not found: {source_name}")
