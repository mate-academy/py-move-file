import os


def move_file(command: str) -> None:
    parts = command.split()

    if command.startswith("mv ") and len(parts) == 3:
        comm, source_file, path = parts
        dir_path = os.path.dirname(path)
        destination_file = os.path.basename(path) or source_file

        if not dir_path and destination_file:
            os.rename(source_file, destination_file)

        if dir_path and destination_file:
            os.makedirs(dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, destination_file)

            with (open(source_file, "r") as source,
                  open(file_path, "w") as destination):
                destination.write(source.read())

            os.remove(source_file)
