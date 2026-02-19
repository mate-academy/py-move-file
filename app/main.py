import os


def move_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "mv":
        print("The command is not correct")
        return

    mv_command, name_in, way = parts
    if way.endswith("/"):
        way = os.path.basename(name_in)

    only_dir = os.path.dirname(way)
    if only_dir:
        os.makedirs(only_dir, exist_ok=True)

    try:
        with open(name_in, "r") as file_in, open(way, "w") as file_out:
            for line in file_in:
                file_out.write(line)
        os.remove(name_in)
    except Exception as e:
        print(f"Error: {e}")
