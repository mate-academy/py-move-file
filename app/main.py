import os


def move_file(command: str) -> None:

    _, source, file_path = command.split(" ")

    directory_path = os.path.dirname(file_path)
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    try:
        with (
            open(source, "r") as source_file,
                open(file_path, "w") as destination_file
        ):
            destination_file.write(source_file.read())
        os.remove(source)
        print(f"File '{source}' moved to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error moving file: {e}")
