import os


def move_file(command: str) -> None:
    command_name, source_file, final_file = command.split()

    if command_name and source_file and final_file and command_name == "mv":
        file_directories, file_name = os.path.split(final_file)

        if file_directories:
            os.makedirs(file_directories, exist_ok=True)

        with (
            open(source_file, "r") as start_file,
            open(final_file, "w") as final_file
        ):
            final_file.write(start_file.read())
        os.remove(source_file)
