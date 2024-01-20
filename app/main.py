import os


def move_file(command: str) -> None:
    comm, source_path, dest_path = command.split()
    if comm != "mv":
        return None
    directory, filename = os.path.split(dest_path)
    if directory == "":
        os.rename(source_path, filename)
    else:
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        os.rename(source_path, dest_path)
