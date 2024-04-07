import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) != 3:
        return

    if command[0] != "mv":
        return

    if command[1] == command[2]:
        return

    second_file_dir = "/".join(command[2].split("/")[:-1])

    if second_file_dir:
        os.makedirs(second_file_dir, exist_ok=True)

    with open(command[1], "r") as file1, open(command[2], "w") as file2:
        file2.write(file1.read())
    os.remove(command[1])
