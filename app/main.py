import os


def move_file(command: str) -> None:
    command_name, old_file, new_file = command.split()
    if command_name != "mv":
        return

    if "/" not in command:
        os.rename(old_file, new_file)

    new_file_path = "/".join(new_file.split("/")[:-1])
    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)

    with open(old_file, "r") as old, open(new_file, "w") as new:
        for text in old:
            new.write(text)

    os.remove(old_file)
