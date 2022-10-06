import os


def move_file(command: str) -> None:
    new_file = command.split()[-1]
    old_file = command.split()[1]
    if "/" in command:
        new_file_path = command.split()
        new_file_path = "/".join(new_file_path[-1].split("/")[:-1])
        new_file = f"{new_file_path}/{command.split('/')[-1]}"

        try:
            os.makedirs(new_file_path)
        except FileExistsError:
            pass

    if "mv" in command:
        with open(old_file, "r") as file, open(new_file, "w") as new_file:
            new_file.write(file.read())
        os.remove(old_file)
