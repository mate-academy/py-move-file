import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError(
            "Invalid command format. Use: mv <source> <destination>"
        )
    source_filename: str = parts[1]

    destination_path: list[str] = parts[2].split("/")
    destination_filename: str = destination_path.pop()
    directory_to_create: str = ""

    if destination_path:
        for folder in destination_path:
            if directory_to_create:
                directory_to_create += f"/{folder}"
            else:
                directory_to_create = folder
            if not os.path.exists(directory_to_create):
                os.mkdir(directory_to_create)

        destination_filename = (
            f"{directory_to_create}/{destination_filename}"
        )

    with (
        open(source_filename, "r") as source_file,
        open(destination_filename, "w") as destination_file
    ):
        destination_file.write(source_file.read())

    os.remove(source_filename)
