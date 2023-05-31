import os


def move_file(command: str) -> None:
    split_command = command.split()

    if len(split_command) == 3:
        comm, file_in, file_path = split_command

        if comm == "mv":
            path, _ = os.path.split(file_path)
            if not path:
                path = "./"
            if file_path.endswith("/"):
                path = file_path
            elif len(path) > 1 and not os.path.exists(path):
                os.makedirs(path, exist_ok=True)

            with open(file_in, "r") as entry_file, open(file_path,
                                                        "w") as new_file:
                new_file.write(entry_file.read())
            os.remove(file_in)
