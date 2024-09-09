import os


def move_file(command: str) -> None:
    current_dir = os.getcwd()
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid format. Use: mv <source> <destination>")

    out_parts, in_parts = (part.split("/") for part in parts[1:])

    out_dirs, out_file = "/".join(out_parts[:-1]), out_parts[-1]

    if len(in_parts) > 1:
        in_dirs = "/".join(in_parts[:-1])
        in_file = in_parts[-1] if in_parts[-1] else out_file
        in_path = os.path.join(current_dir, in_dirs)
        if not os.path.exists(in_path):
            os.makedirs(in_path, exist_ok=True)
    else:
        in_path = current_dir
        in_file = parts[-1]

    full_out_file = os.path.join(current_dir, out_dirs, out_file)
    full_in_file = os.path.join(in_path, in_file)

    simple_rename(full_out_file, full_in_file)


def simple_rename(out_file: str, in_file: str) -> None | FileNotFoundError:
    if not os.path.isfile(out_file):
        raise FileNotFoundError(f"The file '{out_file}' does not exist.")

    with open(out_file, "r") as from_file, open(in_file, "w") as to_file:
        to_file.write(from_file.read())

    os.remove(out_file)
