import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    original_file = parts[1]
    new_file = parts[2]

    if not os.path.exists(original_file):
        return

    if "/" in new_file:
        new_dir = parts[2].split("/")
        os.makedirs("/".join(new_dir[:-1]), exist_ok=True)

    try:
        with open(original_file, "r") as f:
            content = f.read()
    except FileNotFoundError as e:
        print(e)

    try:
        with open(new_file, "w") as f:
            f.write(content)
        os.remove(original_file)
    except Exception as e:
        print(e)
