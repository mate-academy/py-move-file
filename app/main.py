import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) == 3 and command[0] == "mv":
        command, file_in, file_out = command

        directory = os.path.dirname(file_out)

        if not directory:
            os.rename(file_in, file_out)
            return

        if file_out[-1] == "/":
            file_out = os.path.join(directory, file_in)

        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(file_in, "r") as f_in, open(file_out, "w") as f_out:
            f_out.write(f_in.read())

        os.remove(file_in)
