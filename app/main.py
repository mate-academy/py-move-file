import os


def move_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] == "mv" and len(command_list) == 3:
        command_list = command_list[1:]
    original_file = command_list[0]
    file_path = command_list[1]

    if os.sep in file_path or "/" in file_path:
        directory = os.path.dirname(file_path)

        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        if os.path.exists(original_file):
            with open(original_file, "rb") as old_file:

                with open(file_path, "wb") as new_file:
                    new_file.write(old_file.read())

            os.remove(original_file)
    else:
        os.rename(original_file, file_path)
