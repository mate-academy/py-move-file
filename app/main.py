import os


def move_file(command: str) -> None:
    cmd_parts = command.split(" ")
    if len(cmd_parts) != 3:
        raise ValueError(
            "Invalid command: must be -> mv <source> <destination>"
        )
    cmd, source, dest = cmd_parts
    if cmd != "mv":
        raise ValueError("Invalid command: command must be 'mv'")
    if not os.path.exists(source):
        raise FileNotFoundError(f"{source} does not exist")
    if not os.path.isfile(source):
        raise ValueError(
            "Invalid command: source file must be a file, not a directory"
        )
    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(source))
    if os.path.dirname(dest):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(source, "r") as source_file, open(dest, "w") as dest_file:
        dest_file.write(source_file.read())
    os.remove(source)
