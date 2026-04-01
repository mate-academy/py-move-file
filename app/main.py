import os


def move_file(command):
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        return

    source_file = parts[1]
    destination_file = parts[2]

    if not os.path.exists(source_file):
        return

    if source_file == destination_file:
        return

    if destination_file.endswith(os.sep) or destination_file.endswith('/'):
        destination_file = os.path.join(destination_file, os.path.basename(source_file))

    if os.path.isdir(destination_file):
        destination_file = os.path.join(destination_file, os.path.basename(source_file))

    dirpath = os.path.dirname(destination_file)
    if dirpath not in ('', '.'):
        path_parts = dirpath.split(os.sep)
        # Починаємо нарощувати шлях покроково.
        if dirpath.startswith(os.sep):
            current = os.sep
            iter_parts = path_parts[1:]
        elif os.name == 'nt' and ':' in path_parts[0]:
            # Windows: початковий сегмент — диск, наприклад 'C:'
            current = path_parts[0]
            iter_parts = path_parts[1:]
        else:
            current = ''  # починаємо з порожнього, щоб перша ітерація створила 'first_dir'
            iter_parts = path_parts  # всі частини йдуть в ітерацію
        for p in iter_parts:
            current = os.path.join(current, p) if current else p
            try:
                os.mkdir(current)
            except FileExistsError:
                pass

    with open(source_file, "rb") as fsrc:
        with open(destination_file, "wb") as fdst:
            while True:
                chunk = fsrc.read(4096)
                if not chunk:
                    break
                fdst.write(chunk)

    os.remove(source_file)