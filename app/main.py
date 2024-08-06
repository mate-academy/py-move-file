import os


def move_file(command: str) -> None:
    try:
        command, source_path, destination_path = command.split()
        if command != "mv":
            raise ValueError("The command is not 'mv'")
    except ValueError as e:
        raise ValueError("The command is not valid") from e

    if source_path != destination_path:
        _, source_file = os.path.split(source_path)

        destination_path, destination_file = os.path.split(destination_path)
        destination_file = destination_file or source_file
        if destination_path:
            os.makedirs(destination_path, exist_ok=True)
            full_destination_path = os.path.join(
                destination_path, destination_file
            )
        else:
            full_destination_path = destination_file

        with open(source_path, "rb") as source, open(
            full_destination_path, "wb"
        ) as destination:
            destination.write(source.read())
        os.unlink(source_path)
