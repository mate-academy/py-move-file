import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and command[0] == "mv":
        cmd, file_old, file_path = command
        directory, file_name = os.path.split(file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with (
            open(file_old, "r") as file_in,
            open(file_path, "w") as file_out
        ):
            file_out.write(file_in.read())
        os.remove(file_old)
