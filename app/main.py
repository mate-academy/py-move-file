import os


def move_file(command: str) -> None:
    command_key_word, file_in_name, dir_destination = command.split()

    if command_key_word == "mv" and file_in_name != dir_destination:
        *directories, file_out_name = dir_destination.split("/")

        if not directories:
            os.rename(file_in_name, file_out_name)
        else:
            path = os.path.join(*directories)
            os.makedirs(path, exist_ok=True)

            with (
                open(file_in_name, "r") as file_in,
                open(dir_destination, "w") as file_out
            ):
                file_out.write(file_in.read())

            os.remove(file_in_name)
