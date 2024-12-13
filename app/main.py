import os


def move_file(command: str) -> None:
    command_part, source_file, destination_path = command.split()
    if command_part != "mv":
        return
    destination_path, destination_file = os.path.split(destination_path)
    if destination_path:
        destination_path = os.path.join(os.getcwd(), destination_path)
        os.makedirs(destination_path, exist_ok=True)
    with (
        open(source_file, "r") as old_file,
        open(os.path.join(destination_path, destination_file), "w") as new_file
    ):
        new_file.write(old_file.read())
    os.remove(source_file)
