import os


def move_file(command: str) -> None:
    mcommand, file_naming, file_path = command.split()
    if mcommand == "mv":
        if not os.path.dirname(file_path):
            # Destination is just a new file name, rename the file
            os.replace(file_naming, file_path)
        else:
            # Destination is a path, handle it accordingly
            destination_path = os.path.dirname(file_path)

            if not os.path.exists(destination_path):
                os.makedirs(destination_path, exist_ok=True)

            # Check if the file is already in the destination directory
            if not os.path.exists(file_path):
                os.replace(file_naming, file_path)
