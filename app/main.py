import os


def move_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "mv":
        raise ValueError("""Invalid command:
        use 'mv source_path destination_path'""")

    source_path, destination_path = parts[1], parts[2]

    if destination_path.endswith("/"):
        destination_path = os.path.join(
            destination_path,
            os.path.basename(source_path)
        )

    destination_dir = os.path.dirname(destination_path)

    if destination_dir:
        if (
                os.path.exists(destination_dir)
                and not os.path.isdir(destination_dir)
        ):
            raise NotADirectoryError(f"{destination_dir} exists "
                                     f"and is not a directory")

        os.makedirs(destination_dir, exist_ok=True)

    with open(source_path, "r") as src_file:
        content = src_file.read()

    with open(destination_path, "w") as dst_file:
        dst_file.write(content)

    os.remove(source_path)
