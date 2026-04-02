import os


def move_file(command: str) -> None:
    cmd, src, dest = command.split()

    if cmd == "mv" and dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))
    elif cmd == "mv" and not dest.endswith("/"):
        # Checking if dir is exist
        dest_dir = os.path.dirname(dest)
        if dest_dir:
            os.makedirs(dest_dir, exist_ok=True)
    else:
        print("Command is invalid")

    with open(src, "r") as file_in:
        content = file_in.read()

    with open(dest, "w") as file_out:
        file_out.write(content)

    os.remove(src)
