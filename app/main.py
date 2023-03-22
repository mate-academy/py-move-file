import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    cmv, source_path, destination_path = command.split()
    some_dir, new_file = os.path.split(destination_path)
    if some_dir:
        os.makedirs(name=some_dir, exist_ok=True)
    with (
        open(source_path) as source,
        open(destination_path, "w") as destination
    ):
        destination.write(source.read())
    os.remove(source_path)
