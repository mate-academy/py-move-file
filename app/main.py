import os


def move_file(command: str) -> None:
    new_one = command.split()
    if len(new_one) != 3 and new_one[0] != "mv":
        raise ValueError("Invalid command format")

    move, first, second = new_one
    destination = os.path.dirname(second)

    if destination:
        os.makedirs(destination, exist_ok=True)

    new_file = os.path.join(destination, os.path.basename(second))
    with (
        open(first, "r") as file_in,
        open(new_file, "w") as file_out
    ):
        file_out.write(file_in.read())

    if first != new_file:
        os.remove(first)
