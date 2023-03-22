import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return
    mv_, source_path, destination_path = command.split()
    some_dir, new_file = os.path.split(destination_path)
    if some_dir:
        os.makedirs(name=some_dir, exist_ok=True)
    with open(source_path) as s_file, \
            open(os.path.join(destination_path), "w") as n_file:
        n_file.write(s_file.read())
    os.remove(source_path)
