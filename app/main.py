import os


def move_file(command: str) -> None:
    items = command.split()
    if (
            len(items) == 3 and items[0] == "mv"
            and items[1] != items[2]
    ):
        old_file = command.split()[1]
        new_file = command.split()[2]

        new_path, file_name = os.path.split(new_file)
        if len(new_path) != 0:
            os.makedirs(new_path, exist_ok=True)

        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
        os.remove(old_file)
