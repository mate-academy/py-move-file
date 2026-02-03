import os


def move_file(command: str) -> str | None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "mv":
        return None

    _, source_path, destination_path = parts

    if os.path.isdir(destination_path) or destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path, os.path.basename(source_path)
        )

    directory = os.path.dirname(destination_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    if source_path == destination_path:
        return "The source and destination are the same file."

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"File {source_path} not found")

    os.rename(source_path, destination_path)
