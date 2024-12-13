import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv":
        raise ValueError

    file_name = parts[1]
    destination = parts[2]
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"Source file '{file_name}' not found")
    if "/" in destination:
        destination_dir = os.path.dirname(destination)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
        if destination.endswith("/"):
            name = file_name.split("/")[-1]
            destination += name

    with (
        open(file_name, "r") as file_in,
        open(destination, "w") as file_out
    ):
        file_out.write(file_in.read())

    os.remove(file_name)
