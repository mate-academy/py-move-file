import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    mv, source_file, destination_path = parts
    if source_file == destination_path:
        return
    directory = os.path.dirname(destination_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with (open(source_file, "r") as file_in,
          open(destination_path, "w") as file_out):
        file_out.write(file_in.read())
    os.remove(source_file)
