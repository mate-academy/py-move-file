import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        raise ValueError("Invalid command")
    name, source, destination = command.split()

    if destination.endswith("/") or name != "mv":
        raise ValueError("Invalid command")

    separator = destination.rfind("/")
    if separator == -1:
        os.rename(source, destination)
        return

    des_path = destination[: separator]
    os.makedirs(des_path, exist_ok=True)
    with (
        open(source, "r") as file_in,
        open(destination, "w") as file_out
    ):
        file_out.write(file_in.read())

    os.remove(source)
