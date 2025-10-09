import os


def move_file(command: str) -> None:
    arguments = command.split()
    if len(arguments) != 3 or arguments[0] != "mv":
        return
    src, dest = arguments[1], arguments[2]

    if dest == "." or dest == "./":
        dest = os.getcwd()

    if not os.path.isfile(src):
        return

    is_dest_dir = os.path.isdir(dest) or dest.endswith(os.sep)
    if is_dest_dir:
        dest_dir = dest.rstrip(os.sep)
        dest_path = os.path.join(dest_dir, os.path.basename(src))
    else:
        dest_dir = os.path.dirname(dest)
        dest_path = dest

    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)

    os.replace(src, dest_path)
