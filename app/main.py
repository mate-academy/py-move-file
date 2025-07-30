import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    source = parts[1]
    target = parts[2]
    if target.endswith("/"):
        file_name = os.path.basename(source)
        target = os.path.join(target, file_name)
    dir_path = os.path.dirname(target)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path, exist_ok=True)
    with open(source, "rb") as file_in, open(target, "wb") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
