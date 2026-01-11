import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) != 3:
        raise Exception("Invalid command")

    if "mv" != command[0]:
        raise ValueError("Command must start with 'mv '")

    mv, source_path, new_file = command

    if not os.path.exists(source_path) or not os.path.isfile(source_path):
        raise FileNotFoundError(
            f"Source source_path '{source_path}' does not exist"
        )

    if new_file.endswith("/"):
        new_file = os.path.join(new_file, os.path.basename(source_path))

    new_file_dir = os.path.dirname(new_file)
    if new_file_dir:
        os.makedirs(new_file_dir, exist_ok=True)

    with open(source_path, "rb") as f_file:
        content = f_file.read()

    with open(new_file, "wb") as f_new_file:
        f_new_file.write(content)

    os.remove(source_path)
