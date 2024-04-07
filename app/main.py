import os


def move_file(command: str) -> None:
    command, old_file_name, new_file_name = command.split()
    if command != "mv":
        return

    if "/" in new_file_name:
        new_file_path = new_file_name.split("/")
        new_file_path.pop(-1)
        os.makedirs(os.path.join(*new_file_path), exist_ok=True)

    with (open(old_file_name) as old, open(new_file_name, "w") as new):
        new.write(old.read())

    os.remove(old_file_name)
