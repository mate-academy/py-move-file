import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) != 3:
        raise ValueError(
            f"unexpected number of values (expected 3, got {len(command)})"
        )
    if command[0] != "mv":
        raise ValueError(f"{command[0]}: command not found")

    old_file_name = command[1]
    new_file_name = command[2]

    if not os.path.exists(old_file_name):
        raise FileNotFoundError(f"no such file '{old_file_name}'")

    old_file_tail = os.path.split(old_file_name)[1]
    new_file_tail = os.path.split(new_file_name)[1]
    if not old_file_tail:
        raise ValueError(f"'{old_file_name}' is not a file")
    if not new_file_tail:
        raise ValueError(f"'{new_file_name}' is not a file")

    new_file_path = os.path.split(new_file_name)[0]
    if new_file_path:
        os.makedirs(new_file_path, exist_ok=True)

    with (open(old_file_name) as old, open(new_file_name, "w") as new):
        new.write(old.read())

    os.remove(old_file_name)
