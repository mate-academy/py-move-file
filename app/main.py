import os


def move_file(command: str) -> None:

    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Command must be in the format: 'mv <source> <destination>'"
        )

    sourse, destination = parts[1:]

    if destination.endswith("/"):

        destination_dir = destination.rstrip("/")
        if not destination_dir:
            destination_dir = "."
        destination_basename = os.path.basename(sourse)
        destination_path = os.path.join(destination_dir, destination_basename)
    else:
        destination_path = destination
        destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    with open(sourse, "r") as file_sourse, open(
        destination_path, "w"
    ) as file_destination:
        content = file_sourse.read()
        file_destination.write(content)

    os.remove(sourse)
