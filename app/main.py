import os


def move_file(command: str) -> None:
    details = command.split(" ")
    if len(details) != 3 or details[0] != "mv":
        return
    _, current_file, way_with_new_name = details
    if "/" in way_with_new_name:
        *way, new_name = way_with_new_name.split("/")
        folder_path = "/".join(way)
        os.makedirs(folder_path, exist_ok=True)
        os.rename(current_file, way_with_new_name)
    else:
        try:
            os.rename(current_file, way_with_new_name)
        except FileNotFoundError as e:
            raise e
