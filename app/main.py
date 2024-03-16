import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        command_name, file_copy, file_new_path = command

        if command_name == "mv":
            file_path, name = os.path.split(file_new_path)

            if file_path:
                os.makedirs(file_path, exist_ok=True)

        with (
            open(file_copy, "r") as copy,
            open(file_new_path, "w") as move
        ):
            move.write(copy.read())

        os.remove(file_copy)
