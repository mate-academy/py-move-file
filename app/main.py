import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv" or len(parts) != 3:
        print("Invalid command")
        return None

    old_file = parts[1]
    new_file = parts[2]

    path_parts = new_file.split("/")
    if len(path_parts) > 1:
        os.makedirs("/".join(path_parts[:-1]), exist_ok=True)

    try:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            new.write(old.read())

        os.remove(old_file)
    except (OSError, PermissionError) as e:
        print("Error ", e)
        return None
