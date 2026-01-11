import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Invalid command format.")

    key_word, source_file, destination_path = parts

    source_file = os.path.join(source_file)
    destination_path = os.path.join(destination_path)

    if key_word == "mv" and source_file != destination_path:

        destination_folder, new_filename = os.path.split(destination_path)

        if new_filename:
            if destination_folder:
                os.makedirs(destination_folder, exist_ok=True)

            os.rename(source_file, destination_path)
