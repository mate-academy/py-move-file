import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) < 3:
        print("Invalid command format. Usage: mv source_file destination_file")
        return

    source = parts[1]
    file_path = parts[2]

    directory_path = os.path.dirname(file_path)
    if directory_path:
        os.makedirs(directory_path, exist_ok=True)

    try:
        with open(source, "r") as source_file:
            with open(file_path, "w") as destination_file:
                destination_file.write(source_file.read())
        os.remove(source)
        print(f"File '{source}' moved to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error moving file: {e}")
