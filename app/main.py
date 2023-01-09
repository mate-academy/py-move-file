import os


def move_file(command: str) -> None:
    command, source_path, destination_path = command.split()
    if command == "mv" and source_path != destination_path:
        os.makedirs(os.path.dirname(destination_path))
        with (
            open(f"{source_path}", "r") as file_in,
            open(f"{destination_path}", "w") as file_out
        ):
            file_out.write(file_in.read())
            os.remove(source_path)
