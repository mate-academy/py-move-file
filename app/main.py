import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        raise Exception("Command should have 3 arguments")
    if parts[0] != "mv":
        raise Exception("Command should start with 'mv'.")
    if parts[1].endswith("/"):
        raise Exception("Doesnt support directories.")

    src, dst = parts[1], parts[2]

    if dst.endswith("/"):
        dst = os.path.join(dst, os.path.basename(src))

    target_dir = os.path.dirname(dst)
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    with open(src, "r") as f:
        data = f.read()

    os.remove(src)

    with open(dst, "w") as f:
        f.write(data)
