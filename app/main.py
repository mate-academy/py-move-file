import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Command requires `mv old_file new_file` syntax")
        return None

    command_name, old_file, new_file = parts

    if command_name != "mv":
        print("Invalid command")
        return None

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
