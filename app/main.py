import os


def move_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "mv":
        return
    cmd, source_file, destination = command.split()
    new_path = os.path.split(destination)[0]
    new_file_name = os.path.split(destination)[1]

    if not new_path:
        os.rename(source_file, destination)
        return

    os.makedirs(new_path, exist_ok=True)
    os.rename(source_file, os.path.join(new_path, new_file_name))
