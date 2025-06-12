import os


def move_file(command: str) -> None:
    part = command.split()
    old_path = part[1]
    if not os.path.exists(old_path):
        print(f"⚠️Source file '{old_path}' not found.")
        return

    new_path = part[2]
    filename = old_path.split("/")[-1]
    if new_path.endswith("/"):
        final_new_path = new_path + filename
    else:
        final_new_path = new_path

    directory_path = os.path.dirname(final_new_path)
    parts = directory_path.replace("\\", "/").split("/")

    current_path = "."
    for part in parts:
        current_path = os.path.join(current_path, part)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    with open(old_path, "rb") as src:
        content = src.read()

    with open(final_new_path, "wb") as dst:
        dst.write(content)

    os.remove(old_path)
