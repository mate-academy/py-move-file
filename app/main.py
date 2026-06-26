import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    source = parts[1]
    destination = parts[2]
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(source, "r") as file_in:
        content = file_in.read()
    with open(destination, "w") as file_out:
        file_out.write(content)
    os.remove(source)
