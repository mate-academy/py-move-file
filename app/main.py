import os.path


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    source = parts[1]
    destination = parts[2]
    if source == destination:
        return

    if not os.path.exists(source) or not os.path.isfile(source):
        return

    if destination.endswith("/") or os.path.isdir(destination):
        filename = os.path.basename(source)
        full_destination = os.path.join(destination, filename)
    else:
        full_destination = destination

    folder_path = os.path.dirname(full_destination)

    if folder_path:
        os.makedirs(folder_path, exist_ok=True)
    try:
        with open(source, "r") as f, open(full_destination, "w") as d:
            data = f.read()
            d.write(data)
        os.remove(source)
    except Exception:
        return
