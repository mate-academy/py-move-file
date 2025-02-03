import os


def move_file(command: str) -> None:
    parts = command.split()
    source_file = parts[1]
    dest_path = parts[2]

    if os.path.dirname(source_file) == os.path.dirname(dest_path):
        os.rename(source_file, dest_path)
    else:
        dest_dir = os.path.dirname(dest_path)
        os.makedirs(dest_dir, exist_ok=True)

        with open(source_file, "r") as f1:
            text = f1.read()

        with open(dest_path, "w") as f2:
            f2.write(text)

        os.remove(source_file)
