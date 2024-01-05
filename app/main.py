import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] == "mv" and len(parts) == 3:
        source = parts[1]
        destination, filename = os.path.split(parts[2])
        if destination:
            os.makedirs(destination, exist_ok=True)

        with (open(parts[1], "r") as file_in,
              open(os.path.join(destination, filename), "w") as file_out):
            file_out.write(file_in.read())

        os.remove(source)
