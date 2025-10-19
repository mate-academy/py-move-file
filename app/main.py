import os


def move_file(command: str) -> None:
    if not command.startswith("mv "):
        return

    _, source_file, target_path = command.split()
    if target_path.endswith("/"):
        target_path = os.path.join(target_path, os.path.basename(source_file))

    directory = os.path.dirname(target_path)
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

    with open(source_file, "r") as file_in, open(target_path, "w") as file_out:
        for line in file_in:
            file_out.write(line)
    os.remove(source_file)
