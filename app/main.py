import os


def move_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "mv":
        return

    source_path = parts[1]
    destination_patch = parts[2]

    if destination_patch.endswith("/"):
        file_name = os.path.basename(source_path)
        full_destination_path = destination_patch + file_name
    else:
        full_destination_path = destination_patch

    dest_dir = os.path.dirname(full_destination_path)

    if dest_dir:
        os.makedirs(dest_dir,exist_ok=True)

    try:
        with open(source_path, "r") as file_in, open(full_destination_path, "w") as file_out:
            content = file_in.read()
            file_out.write(content)

        os.remove(source_path)
    except FileNotFoundError:
        print(f"Error: Source file '{source_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
