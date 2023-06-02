import os


def move_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) == 3:
        command, file_in, file_path = split_command

        if command == "mv":
            path, _ = os.path.split(file_path)
            if path:
                os.makedirs(path, exist_ok=True)

            with open(file_in, "r") as entry_file, open(file_path,
                                                        "w") as new_file:
                new_file.write(entry_file.read())
            os.remove(file_in)
