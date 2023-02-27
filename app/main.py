import os


def move_file(command: str) -> None:
    if len(command) != 3:
        cmd, filename, destination_path_with_file = command.split()
        if cmd == "mv" and filename != destination_path_with_file:
            os.makedirs(
                os.path.dirname(destination_path_with_file),
                exist_ok=True
            )
            with (
                open(f"{filename}", "r") as file_in,
                open(f"{destination_path_with_file}", "w") as file_out
            ):
                file_out.write(file_in.read())
                os.remove(filename)
