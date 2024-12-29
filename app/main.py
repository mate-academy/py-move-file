import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3 or parts[0] != "mv":
        raise ValueError("Invalid command format. Use"
                         " 'mv source_path destination_path'.")

    source_path, destination_path = parts[1], parts[2]

    if not os.path.isfile(source_path):
        raise FileNotFoundError(f"Source file '{source_path}' "
                                f"does not exist.")
    split_file_extension = os.path.splitext(destination_path)
    if not split_file_extension[-1]:
        destination_path = os.path.join(destination_path, source_path)

    directory_path = os.path.dirname(destination_path)
    if directory_path and not os.path.exists(directory_path):
        os.makedirs(directory_path, exist_ok=True)

    with (open(source_path, "r") as src_file,
          open(destination_path, "w") as dest_file):
        dest_file.write(src_file.read())
    os.remove(source_path)
