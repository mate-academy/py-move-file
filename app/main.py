import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError

    command, old_file, new_file = command.split()

    if command == "mv":
        new_file_path, new_file_name = os.path.split(new_file)

        if len(new_file_path) > 0:
            os.makedirs(new_file_path, exist_ok=True)

        if len(new_file_name) == 0:
            new_file_name = old_file

        destination_path = os.path.join(new_file_path, new_file_name)

        with (
            open(old_file, "r") as file_old,
            open(destination_path, "w") as file_copy
        ):
            file_copy.write(file_old.read())

        os.remove(old_file)
