import os


def move_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) == 3:
        command_name, source_filepath, target_filepath = command_split

        # Check if the command is 'mv' and that the source
        # and target are different
        if command_name == "mv" and source_filepath != target_filepath:

            # Ensure the target directory exists
            try:
                if target_filepath.endswith("/"):
                    os.makedirs(target_filepath, exist_ok=True)
                else:
                    target_dir = os.path.dirname(target_filepath)
                    if target_dir and not os.path.exists(target_dir):
                        os.makedirs(target_dir, exist_ok=True)
            except OSError as e:
                print(f"Error creating target directory: {e}")
                return

            # Move the file
            try:
                with (open(source_filepath, "r") as file_in,
                      open(target_filepath, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print(f"Source file '{source_filepath}' not found.")
                return
            except PermissionError:
                print(f"Permission denied while "
                      f"accessing '{source_filepath}' or "
                      f"'{target_filepath}'.")
                return
            except IOError as e:
                print(f"Error reading from '{source_filepath}' "
                      f"or writing to '{target_filepath}': {e}")
                return

            # Remove the source file after successful move
            try:
                os.remove(source_filepath)
            except FileNotFoundError:
                print(f"Source file '{source_filepath}' already deleted.")
            except PermissionError:
                print(f"Permission denied while deleting '{source_filepath}'.")
            except OSError as e:
                print(f"Error deleting '{source_filepath}': {e}")
