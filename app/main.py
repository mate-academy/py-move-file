import os


def move_file(command: str) -> None:
    command = command.split(" ")
    if "mv" not in command or len(command) != 3:
        return

    if "/" not in command[2]:
        os.rename(command[1], command[2])
        return

    if os.path.exists(command[2]):
        return

    file_name = command[1]
    new_file_name = os.path.split(command[2])[1]
    path = os.path.split(command[2])[0]

    os.makedirs(path, exist_ok=True)

    path = os.path.join(path, new_file_name)

    with (
        open(file_name, "r") as old_file,
        open(path, "w") as new_file
    ):
        new_file.write(old_file.read())

    os.remove(file_name)
