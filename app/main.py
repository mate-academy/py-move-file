import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, source, destination = parts
    if not os.path.exists(source):
        return

    if destination.endswith("/") or os.path.isdir(destination):
        filename = os.path.basename(source)
        target_path = os.path.join(destination, filename)
    else:
        target_path = destination

        # 3. Przygotowanie folderów nadrzędnych
    directory = os.path.dirname(target_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    # 4. Bezpieczna operacja kopiowania i usuwania
    try:
        with open(source, "r") as f_in:
            content = f_in.read()

        with open(target_path, "w") as f_out:
            f_out.write(content)

        # 5. Usuwamy oryginał TYLKO, jeśli zapis się udał
        os.remove(source)

    except (FileNotFoundError, IOError):
        # Usunięto print() - czysty kod bez debugowania
        pass
