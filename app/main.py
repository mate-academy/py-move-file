import os


def move_file(command: str) -> None:
    try:
        command, source, destination = command.split()
    except ValueError:
        print("Three arguments expected")
        return
    if command != "mv" or source == destination:
        return
    if not os.path.exists(source):
        raise FileNotFoundError("Source file does not exist")

    if "/" not in destination:
        os.rename(source, destination)
        return

    directories = os.path.split(destination)[0]
    os.makedirs(directories, exist_ok=True)
    with open(source) as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
    os.remove(source)
