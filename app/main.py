import os


def move_file(command: str) -> None:
    details = command.split(" ")
    if len(details) != 3 or details[0] != "mv":
        return
    _, current_file, way_with_new_name = details
    if way_with_new_name.endswith(os.sep):
        folder_path = way_with_new_name.rstrip(os.sep)
        os.makedirs(folder_path, exist_ok=True)
        destination = os.path.join(folder_path, os.path.basename(current_file))
    else:
        folder_path = os.path.dirname(way_with_new_name)
        if folder_path:
            os.makedirs(folder_path, exist_ok=True)
        destination = way_with_new_name
    os.rename(current_file, destination)
