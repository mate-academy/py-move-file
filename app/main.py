import os


def move_file(command: str) -> None:
    commands = command.split()

    if len(commands) != 3 or commands[0] != "mv":
        raise ValueError(f"'{command}': invalid command input")

    old_file_name, new_file_name = commands[1:]

    old_file_tail = os.path.split(old_file_name)[1]
    new_file_tail = os.path.split(new_file_name)[1]
    if not old_file_tail or not new_file_tail:
        raise ValueError(f"'{command}' must contain two file names")

    new_file_path = os.path.split(new_file_name)[0]
    if new_file_path:
        os.makedirs(new_file_path, exist_ok=True)

    try:
        with open(old_file_name) as old, open(new_file_name, "w") as new:
            new.write(old.read())
    except OSError:
        raise

    os.remove(old_file_name)
