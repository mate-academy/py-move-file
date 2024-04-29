import os


def move_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3 or commands[0] != "mv":
        raise ValueError(f"'{command}': invalid command input")
    old_file, new_file = commands[1:]
    if not os.path.exists(old_file):
        raise ValueError(f"'{old_file}': file does not exist")

    new_file_path, new_file_tail = os.path.split(new_file)
    if not new_file_tail:
        new_file = os.path.join(new_file_path, os.path.split(old_file)[1])
    if new_file_path:
        os.makedirs(new_file_path, exist_ok=True)
    try:
        with open(old_file) as old, open(new_file, "w") as new:
            new.write(old.read())
    except OSError:
        raise

    os.remove(old_file)
