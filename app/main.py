import os
import shutil


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Command must have the format: mv SOURCE DESTINATION")

    _, source_file_path, destination_path = command_parts
    if destination_path.endswith(("/", os.sep)) or (
        os.altsep is not None and destination_path.endswith(os.altsep)
    ):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_file_path)
        )

    destination_directory = os.path.dirname(destination_path)
    if destination_directory:
        normalized_directory = os.path.normpath(destination_directory)
        drive, directory_path = os.path.splitdrive(normalized_directory)
        directory_parts = directory_path.split(os.sep)
        directory_prefix = os.sep if directory_path.startswith(os.sep) else ""
        directory_path = drive + directory_prefix

        for directory_name in directory_parts:
            if not directory_name:
                continue

            directory_path = os.path.join(directory_path, directory_name)
            if not os.path.exists(directory_path):
                os.mkdir(directory_path)

    shutil.copy2(source_file_path, destination_path)
    os.remove(source_file_path)
