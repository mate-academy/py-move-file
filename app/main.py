import os


def move_file(command: str) -> None:
    try:
        command, source, destination = command.split()
    except ValueError:
        raise ValueError("Three arguments expected")
    if command != "mv" or source == destination:
        return
    if not os.path.exists(source):
        raise FileNotFoundError("Source file does not exist")

    directories, file_name = os.path.split(destination)
    if not directories:
        os.rename(source, destination)
        return

    directories = os.path.join(directories)
    os.makedirs(directories, exist_ok=True)

    destination = os.path.join(directories, file_name)
    with open(source) as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
