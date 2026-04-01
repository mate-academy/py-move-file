import os


def move_file(command: str) -> None:
    tokens = command.split()

    if len(tokens) != 3 or tokens[0] != "mv":
        print("Invalid command")
        return

    _, source_file, destination_file = tokens

    if not os.path.dirname(destination_file):
        os.replace(source_file, destination_file)
    else:
        destination_path = os.path.dirname(destination_file)
        os.makedirs(destination_path, exist_ok=True)
        os.replace(source_file, destination_file)
