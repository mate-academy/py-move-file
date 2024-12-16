from os import path, remove, makedirs


def move_file(command: str) -> None:
    command_words = command.split(" ")

    if len(command_words) != 3 or command_words[0] != "mv":
        raise ValueError(
            f"{command} is invalid. Pls, use 'mv source destination'"
        )

    if not path.exists(command_words[1]):
        raise FileNotFoundError(f"File {command_words[1]} not found")

    _, source_file, destination = command_words

    destination = path.normpath(destination)

    if path.isdir(destination):
        path_to_create = destination
        new_filename = path.basename(source_file)
    else:
        path_to_create, new_filename = path.split(destination)

    if path_to_create:
        makedirs(path_to_create, exist_ok=True)

    new_file_path = path.join(path_to_create, new_filename)

    with (
        open(source_file, "r") as source,
        open(new_file_path, "w") as copy
    ):
        copy.write(source.read())

    remove(source_file)
