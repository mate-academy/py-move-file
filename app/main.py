import os


def move_file(command: str) -> None:
    parts_of_command = command.split()

    if len(parts_of_command) == 3 and parts_of_command[0] == "mv":
        (instruction, source_file, dest_file) = parts_of_command

        if dest_file.endswith("/"):
            dest_file += source_file

        if "/" in dest_file:
            os.makedirs(os.path.dirname(dest_file), exist_ok=True)

        with open(dest_file, "w") as file1, open(source_file, "r") as file2:
            file1.write(file2.read())

        os.remove(source_file)
