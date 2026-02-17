import os


def move_file(command: str) -> None:
    content = command.split()
    if len(content) < 3:
        return "Not enough params"
    mv, old_path, new_path = content
    if mv != "mv":
        return "Wrong command"
    if old_path == new_path:
        return
    directories = new_path.split("/")[:-1]
    if directories:
        os.makedirs("/".join(directories), exist_ok=True)
    with open(old_path, "r") as f1, open(new_path, "w") as f2:
        f2.write(f1.read())
    os.remove(old_path)
