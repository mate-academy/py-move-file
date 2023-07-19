import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    if command.split()[0] != "mv":
        return
    cmd, file_from, file_to = command.split()
    if "/" in file_to:
        first_part, second_part = os.path.split(file_to)
        os.makedirs(first_part, exist_ok=True)
        with open(file_from, "r") as file_from, open(file_to, "w") as file_to:
            file_to.write(file_from.read())

        os.remove(file_from)
    else:
        os.rename(file_from, file_to)
