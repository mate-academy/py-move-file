import os


def move_file(command: str) -> None:
    command = command.split()

    if "mv" != command[0]:
        raise ValueError("Command must start with 'mv '")

    if len(command) != 3:
        raise Exception("Invalid command")

    mv, file, new_file = command

    if not os.path.exists(file) or not os.path.isfile(file):
        raise FileNotFoundError(f"Source file '{file}' does not exist")

    if new_file.endswith("/"):
        new_file = os.path.join(new_file, os.path.basename(file))

    new_file_dir = os.path.dirname(new_file)
    if new_file_dir:
        os.makedirs(new_file_dir, exist_ok=True)

    with open(file, "rb") as f_file:
        content = f_file.read()

    with open(new_file, "wb") as f_new_file:
        f_new_file.write(content)

    os.remove(file)
