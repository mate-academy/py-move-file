import os
import shutil


def move_file(command: str) -> str:
    try:
        parts = command.strip().split()

        if len(parts) != 3:
            return ("Error: Command must "
                    "have exactly 3 parts: "
                    "mv source destination")

        if parts[0] != "mv":
            return "Error: Command must start with mv"

        _, source_path, destination_path = parts

        if not source_path or not destination_path:
            return ("Error: Source and destination paths "
                    "cannot be empty")

        if not os.path.exists(source_path):
            return (f"Error: Source file "
                    f"{source_path} does not exist")

        if not os.path.isfile(source_path):
            return f"Error: {source_path} is not a file"

        destination_is_directory = destination_path.endswith("/")

        if destination_is_directory:
            destination_path = destination_path.rstrip("/")

        source_filename = os.path.basename(source_path)

        if destination_is_directory:
            destination_dir = destination_path
        else:
            destination_dir = os.path.dirname(destination_path)

        if destination_dir and not os.path.exists(destination_dir):
            try:
                os.makedirs(destination_dir, exist_ok=True)
            except OSError as e:
                return (f"Error: Failed to create "
                        f"directories {destination_dir}: {e}")

        if destination_is_directory:
            final_destination_path = (
                os.path.join(destination_path, source_filename))
        else:
            final_destination_path = destination_path

        shutil.copy2(source_path, final_destination_path)

        os.remove(source_path)

        return (f"Success: Moved {source_path} "
                f"to {final_destination_path}")

    except Exception as e:
        return f"Error: Unexpected error occurred: {e}"
