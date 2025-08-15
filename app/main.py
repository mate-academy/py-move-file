import os


def move_file(command: str) -> None:
    if command == "":
        return

    file_names = command.split(" ")
    if len(file_names) != 3 or file_names[0] != "mv":
        return

    source_file = file_names[1]
    if "/" in source_file:
        return

    target_path = file_names[2]

    if "/" in target_path:
        target_dir = os.path.dirname(target_path)

        dirs = target_dir.split("/")
        current_path = ""
        for dir_name in dirs:
            if current_path:
                current_path = current_path + "/" + dir_name
            else:
                current_path = dir_name

            if not os.path.exists(current_path):
                os.mkdir(current_path)

        if os.path.exists(source_file):
            with open(source_file, "r") as file_in:
                content = file_in.read()

            with open(target_path, "w") as file_out:
                file_out.write(content)

            os.remove(source_file)

    elif os.path.exists(source_file) and source_file != target_path:
        with open(source_file, "r") as file_in:
            content = file_in.read()

        with open(target_path, "w") as file_out:
            file_out.write(content)

        os.remove(source_file)
