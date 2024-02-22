import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command format. Usage: mv source_file destination_path")
        return

    source, destination = parts[1], parts[2]

    destination_dir = os.path.dirname(destination)
    if destination_dir and not os.path.exists(destination_dir):
        os.makedirs(destination_dir, exist_ok=True)

    with open(source, "r") as f_src:
        with open(destination, "w") as f_dst:
            f_dst.write(f_src.read())

    os.remove(source)
