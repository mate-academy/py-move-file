import os


def move_file(command: str) -> None:
    # Check if input command format is correct
    if not is_input_data_correct(command):
        return

    # Get correct paths for source and destination files
    origin_input_path, dest_input_path = command.split()[1:]
    dest_short_path, dest_file_name = os.path.split(dest_input_path)
    origin_short_path, origin_file_name = os.path.split(origin_input_path)
    if not dest_file_name:
        dest_full_path = os.path.join(dest_short_path, origin_file_name)
    else:
        dest_full_path = dest_input_path

    # If new location is not provided:
    # Rename source file
    if not origin_short_path and not dest_short_path:
        rename_file(origin_file_name, dest_file_name)
        return

    # If new location is provided:
    # Open source file for reading
    try:
        origin_file = open(origin_input_path, "r")
    except FileNotFoundError:
        print(f"No source file with such name: {origin_input_path}")
        return
    except PermissionError:
        print(f'"{origin_file_name}" is a folder')
        return

    # Create folder tree given in the destination path
    try:
        os.makedirs(dest_short_path, exist_ok=True)
    except OSError:
        print(r'File name cannot contain the following characters: \/?*:"<>|')
        return

    # Create target file, copy data to it from source file, remove source file
    dest_full_path = os.path.normpath(dest_full_path)
    try:
        with open(dest_full_path, "w") as dest_file:
            dest_file.write(origin_file.read())
    except FileNotFoundError:
        print(f"Incorrect file name or path: {dest_input_path}")
        return
    except FileExistsError:
        print(f"{dest_full_path} already exists")
        return
    except PermissionError:
        print(f'"{dest_file_name}" is a folder')
    except OSError:
        print(r'File name cannot contain the following characters: \/?*:"<>|')
        return
    else:
        origin_file.close()
        os.remove(origin_input_path)


def rename_file(old_file: str, new_file: str) -> None:
    try:
        os.rename(old_file, new_file)
    except FileNotFoundError:
        print(f"No source file with such name: {old_file}")
    except FileExistsError:
        print(f"{new_file} already exists")


def is_input_data_correct(command_text: str) -> bool:
    try:
        command_name, origin_path, destination_path = command_text.split()
    except ValueError:
        print(r"Correct input format: <command> <origin file path/name> "
              r"<destination file path/name>")
        return False

    if command_name != "mv":
        print("Incorrect command name. Type 'mv' for move.")
        return False

    if origin_path == destination_path:
        print("Nothing to move.")
        return False

    return True
