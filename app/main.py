import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("Невірний формат команди. "
                         "Використовуйте 'mv <source> <destination>'.")

    _, source, destination = parts

    if not os.path.exists(source):
        raise FileNotFoundError(f"Файл '{source}' не знайдено.")
    if os.path.isdir(source):
        raise IsADirectoryError(f"Джерело '{source}' є "
                                "каталогом, а не файлом.")

    if destination.endswith("/"):
        final_destination = os.path.join(destination, os.path.basename(source))
    else:
        final_destination = destination

    destination_dir = os.path.dirname(final_destination)
    if destination_dir:
        path_parts = []
        while destination_dir and not os.path.exists(destination_dir):
            path_parts.append(os.path.basename(destination_dir))
            destination_dir = os.path.dirname(destination_dir)

        for part in reversed(path_parts):
            destination_dir = os.path.join(destination_dir, part)
            os.mkdir(destination_dir)

    with open(source, "r") as infile:
        content = infile.read()
    with open(final_destination, "w") as outfile:
        outfile.write(content)

    os.remove(source)
