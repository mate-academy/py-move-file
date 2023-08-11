import os


def move_file(command: str) -> None | str:
    if len(command.split()) != 3:
        return "Incorrect statement printed"

    cmd, current_file, destination = command.split()

    if cmd != "mv":
        return "Command is incorrect"

    dir_path, new_file_name = os.path.split(destination)

    try:
        os.makedirs(dir_path, exist_ok=True)
    except FileNotFoundError:
        print("Not needed to create folders")

    try:
        with open(current_file, "r") as source_file, open(
            destination, "w"
        ) as moved_file:
            moved_file.write(source_file.read())
    except FileNotFoundError:
        return f"Source file '{current_file}' not found"

    os.remove(current_file)
