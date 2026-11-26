import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, source, target = parts
    if target.endswith("/"):
        target = os.path.join(target, source)
    directory = os.path.dirname(target)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(source) as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
