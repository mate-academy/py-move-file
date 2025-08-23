import os


def move_file(command: str) -> None:
    parts = command.split(" ", 2)
    if len(parts) != 3 or parts[0] != "mv":
        return

    _, source_path, destination_path = parts

    if destination_path.endswith("/"):
        target_directory = destination_path.rstrip("/")
        target_filename = os.path.basename(source_path)
        final_path = target_directory + "/" + target_filename
    else:
        final_path = destination_path
        target_directory = os.path.dirname(final_path)

    if target_directory:
        os.makedirs(target_directory, exist_ok=True)

    with open(source_path, "rb") as source_file_object, \
         open(final_path, "wb") as destination_file_object:
        destination_file_object.write(source_file_object.read())

    os.remove(source_path)
