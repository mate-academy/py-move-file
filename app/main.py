import os


def move_file(command: str) -> None:
    new_line = command.strip().split()

    if len(new_line) != 3 or new_line[0] != "mv":
        raise ValueError

    source_file = new_line[1]
    place_file = new_line[2]

    if not os.path.exists(source_file):
        raise FileNotFoundError(f"Source file '{source_file}' not found")

    if place_file.endswith("/"):
        if not os.path.exists(place_file):
            os.makedirs(place_file, exist_ok=True)
        place_file = os.path.join(place_file, os.path.basename(source_file))
    else:
        place_file_dir = os.path.dirname(place_file)
        if place_file_dir and not os.path.exists(place_file_dir):
            os.makedirs(place_file_dir, exist_ok=True)

    if os.path.exists(place_file):
        os.remove(place_file)

    try:
        os.rename(source_file, place_file)
        print(f"Moved file from {source_file} to {place_file}")
    except OSError as e:
        print(f"Error moving file: {e}")
