import os


def move_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) != 3 or command_parts[0] != "mv":
        raise ValueError("Invalid command")

    if not os.path.isfile(command_parts[1]):
        raise FileNotFoundError(f"Source file '{command_parts[1]}' "
                                f"does not exist")

    _, source_path, dest_path = command_parts

    with open(source_path , "r") as source_file:
        content = source_file.read()

    if os.path.dirname(dest_path) != "":
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    if os.path.basename(dest_path).find(".") == -1:
        load_path = os.path.join(dest_path, os.path.basename(source_path))
    else:
        load_path = dest_path

    with open(load_path, "w") as dest_file:
        dest_file.write(content)

    if source_path != load_path:
        os.remove(source_path)
