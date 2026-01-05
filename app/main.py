import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. "
                         "Use: mv <source> <destination>")
    _, source_path, dest_path = parts
    if dest_path.endswith("/"):
        filename = os.path.basename(source_path)
        dest_path = os.path.join(dest_path, filename)
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir, exist_ok=True)
    try:
        with open(source_path, "r") as f_src:
            content = f_src.read()
        with open(dest_path, "w") as f_dest:
            f_dest.write(content)
        os.remove(source_path)
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied accessing "
              f"'{source_path}' or '{dest_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
