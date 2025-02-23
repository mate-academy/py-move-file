import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Command must be in the format: 'move from_f to_f'")

    _, from_f, to_f = parts
    current_dir = os.path.dirname(to_f) or "."

    os.makedirs(current_dir, exist_ok=True)

    new_file_path = os.path.join(current_dir, os.path.basename(to_f))

    with open(from_f, "r") as src_file, open(new_file_path, "w") as dst_file:
        dst_file.write(src_file.read())

    os.remove(from_f)
