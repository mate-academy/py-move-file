import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        print("Error: Invalid command format.")
        return

    cmd, source_file, destination = parts

    if cmd != "mv":
        print("Error: Command must start with 'mv'.")
        return

    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' does not exist.")
        return

    path_parts = destination.split("/")

    if destination.endswith("/"):
        filename = os.path.basename(source_file)
        dir_parts = path_parts[:-1] if path_parts[-1] == "" else path_parts
    else:
        filename = path_parts[-1]
        dir_parts = path_parts[:-1]

    current_path = ""
    for i, part in enumerate(dir_parts):
        if current_path:
            current_path = os.path.join(current_path, part)
        else:
            current_path = part

        try:
            os.mkdir(current_path)
        except FileExistsError:
            pass
        except OSError as e:
            print(f"Error: Could not create directory '{current_path}'. {e}")
            return

    if current_path:
        new_file_path = os.path.join(current_path, filename)
    else:
        new_file_path = filename

    try:
        with open(source_file, "r") as original_file:
            file_content = original_file.read()

        with open(new_file_path, "w") as new_file:
            new_file.write(file_content)

        os.remove(source_file)

    except Exception as e:
        print(f"Error: File operation failed. {e}")
