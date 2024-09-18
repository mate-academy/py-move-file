import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        raise ValueError("Command must have exactly 3 arguments")
    mv, source_file, result = parts
    if "/" in result:
        destination, file = os.path.split(result)
    else:
        destination, file = "", result

    if destination:
        os.makedirs(destination, exist_ok=True)

    with (
        open(source_file, "r") as file_in,
        open(os.path.join(destination, file), "w")
        as file_out
    ):
        file_out.write(file_in.read())

    os.remove(source_file)
