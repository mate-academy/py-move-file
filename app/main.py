import os


def move_file(command: str) -> None:

    try:
        cmd, source, destination = command.split()
    except ValueError:
        print("Error!")

    if source == destination:
        return

    if cmd != "mv":
        raise ValueError("Incorrect command!")

    if destination.endswith("/"):
        os.makedirs(destination, exist_ok=True)
        destination = os.path.join(destination, source)
    else:
        dir_name = os.path.dirname(destination)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

    with (open(source, "r") as file_in,
          open(destination, "w") as file_out):
        content = file_in.read()
        file_out.write(content)

    os.remove(source)
