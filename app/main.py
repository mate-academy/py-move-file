import os


def move_file(command: str) -> None:
    command_words = command.split(" ")

    if len(command_words) != 3 or command_words[0] != "mv":
        raise ValueError(
            f"{command} is invalid. Pls, use 'mv source destination'"
        )

    if not os.path.exists(command_words[1]):
        raise FileNotFoundError(f"File {command_words[1]} not found")

    _, source_file, destination = command_words

    destination = os.path.normpath(destination)

    if os.path.isdir(destination):
        path_to_create = destination
        new_filename = os.path.basename(source_file)
    else:
        path_to_create, new_filename = os.path.split(destination)

    if path_to_create:
        os.makedirs(path_to_create, exist_ok=True)

    new_file_path = os.path.join(path_to_create, new_filename)

    with (
        open(source_file, "r") as source,
        open(new_file_path, "w") as copy
    ):
        copy.write(source.read())

    os.remove(source_file)
