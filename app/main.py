import os


def move_file(command: str) -> None:
    parts_of_command = command.split()

    if len(parts_of_command) == 3 and parts_of_command[0] == "mv":
        (instruction, file_in, file_out) = parts_of_command

        if "/" in file_out:
            os.makedirs(os.path.dirname(file_out), exist_ok=True)

        with open(file_out, "w") as f1, open(file_in, "r") as f2:
            f1.write(f2.read())

        os.remove(file_in)
