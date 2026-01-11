import os


def make_directories(destination: str) -> None:
    directory = os.path.split(destination)[0]
    path = os.path.join(directory)
    os.makedirs(path, exist_ok=True)


def copy_file(source: str, destination: str) -> None:
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        copy_content = file_in.read()
        file_out.write(copy_content)


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Invalid command format")

    cmd, source, destination = command.split()

    if cmd != "mv":
        raise ValueError("Invalid command")

    if source == destination:
        return

    if not destination.count("/"):
        os.rename(source, destination)
    else:
        make_directories(destination)
        copy_file(source, destination)
        os.remove(source)
