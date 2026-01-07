import os


def move_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        raise IndexError
    cmd, source, dest_parts = split_command
    if split_command[0] != "mv":
        raise SyntaxError
    file_name = os.path.basename(source)
    if dest_parts.endswith(os.sep):
        target_file_path = os.path.join(dest_parts, file_name)
    else:
        target_file_path = dest_parts
    target_dir = os.path.dirname(target_file_path)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    with open(source, "rb") as old, open(target_file_path, "wb") as new:
        new.write(old.read())
    os.remove(source)
