import os


def move_file(command: str) -> None:
    components = command.split()
    if len(components) != 3 or components[0] != "mv":
        print("Invalid command format. "
              "Please provide a command like "
              "'mv file.txt first_dir/second_dir/file2.txt'.")
        return

    source_path, destination_path = components[1], components[2]
    print(f"source_path: {source_path}")
    print(f"destination_path: {destination_path}")

    path = os.path.dirname(destination_path)
    if path:
        os.makedirs(path, exist_ok=True)
    os.replace(source_path, destination_path)

    print(f"Moved '{source_path}' to '{destination_path}'.")
