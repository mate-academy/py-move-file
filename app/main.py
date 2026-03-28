import os


def move_file(command: str) -> None:
    part = command.split()
    if (
        len(part) == 3
        and part[0] == "mv"
        and part[1] != part[2]
    ):
        old_file_name = part[1]
        destination, new_file_name = os.path.split(part[2])
        if destination:
            os.makedirs(destination, exist_ok=True)
        new_file_path = part[2]
        with (
            open(new_file_path, "w") as new_file,
            open(old_file_name, "r") as old_file
        ):
            new_file.write(old_file.read())
        os.remove(old_file_name)
