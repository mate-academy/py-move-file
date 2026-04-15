import os


def move_file(command: str) -> None:
    parts = command.split()
    source = parts[1]
    destination = parts[2]
    if destination[-1] == "/":
        destination += source
    print(source)
    print(destination)
    directory = os.path.dirname(destination)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(source, "r") as file_1, open(destination, "w") as file_2:
        file_2.write(file_1.read())
    os.remove(source)
