import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        (
            input_command,
            source_file_path,
            destination_file_path
        ) = command.split()
        if input_command == "mv" and source_file_path != destination_file_path:
            new_file_name = destination_file_path.split("/")[-1]
            directory = destination_file_path.split("/")[:-1]
            path = ""
            for folder in directory:
                path += folder + "/"
                os.makedirs(path, exist_ok=True)
            with (
                open(source_file_path, "r") as file_to_move,
                open(os.path.join(path, new_file_name), "w") as file_copy
            ):
                file_copy.write(file_to_move.read())
            os.remove(source_file_path)
