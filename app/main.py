import os


def move_file(command: str) -> None:
    command = command.split()
    if len(command) == 3 and "mv" in command:
        command_name, file, direct = command
        if "/" in direct:
            directory = os.path.split(direct)
            os.makedirs(f"{directory}", exist_ok=True)

        with (open(file, "r") as file_in,
                open(f"{direct}", "w") as file_out):
            file_out.write(file_in.read())
        os.remove(file)
