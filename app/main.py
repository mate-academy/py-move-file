import os


def move_file(command: str) -> None:

    if not command:
        return

    splitted = command.split()

    if len(splitted) != 3:
        return

    if splitted[0] != "mv":
        return

    source_file = splitted[1]

    full_destination = splitted[2].split("/")

    *dirs, new_file_name = full_destination

    if splitted[2].endswith("/"):
        new_file_name = source_file

    current_path = "/".join(dirs)

    os.makedirs(current_path, exist_ok=True)

    with open(source_file, "r") as file:
        content = file.read()
        with open(os.path.join(current_path, new_file_name), "w") as file2:
            file2.write(content)
            os.remove(source_file)
