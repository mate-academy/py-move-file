import os


def move_file(command: str) -> None:
    command_parts = command.strip().split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        print("Error: Invalid command format. Use 'mv source destination'")
        return

    source, destination = command_parts[1], command_parts[2]

    if destination.endswith("/"):
        dest_dir = destination.rstrip("/")
        dest_file = os.path.basename(source)
    else:
        dest_dir = os.path.dirname(destination)
        dest_file = os.path.basename(destination)

    if dest_dir:
        try:
            os.makedirs(dest_dir, exist_ok=True)
        except OSError:
            print(f"Error: Cannot create directory '{dest_dir}'")
            return

    full_dest_path = os.path.join(
        dest_dir, dest_file
    ) if dest_dir else dest_file

    try:
        os.rename(source, full_dest_path)
    except (FileNotFoundError, OSError):
        try:
            with open(source, "rb") as src_file:
                content = src_file.read()
            with open(full_dest_path, "wb") as dest_file:
                dest_file.write(content)
            os.remove(source)
        except FileNotFoundError:
            print(f"Error: Source file '{source}' does not exist")
            return
        except OSError as e:
            print(f"Error: Cannot move file: {str(e)}")
            return
