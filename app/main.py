import os


def move_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "mv" or len(parts) != 3:
        print("Error: command is not correct")
        return

    source = parts[1]
    new = parts[2]

    if not os.path.isfile(source):
        print(f"Error: source file '{source}' does not exist.")
        return

    new_dir = os.path.dirname(new)
    if not os.path.exists(new_dir):
        if new_dir != "":
            os.makedirs(new_dir)

    with open(source, "r") as source_file:
        with open(new, "w") as new_file:
            new_file.write(source_file.read())
    os.remove(source)
