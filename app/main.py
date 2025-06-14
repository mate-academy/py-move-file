import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command format. Expected: mv source destination")
        return

    source_path = parts[1]
    destination_path = parts[2]

    if not os.path.exists(source_path):
        print(f"⚠️ Source file '{source_path}' not found.")
        return

    filename = os.path.basename(source_path)
    if destination_path.endswith("/") or os.path.isdir(destination_path):
        final_destination = os.path.join(destination_path, filename)
    else:
        final_destination = destination_path

    directory_to_create = os.path.dirname(final_destination)
    if not os.path.exists(directory_to_create):
        try:
            os.makedirs(directory_to_create)
        except OSError as e:
            print(f"❌ Failed to create directory '{directory_to_create}': {e}")
            return

    try:
        with open(source_path, "rb") as src:
            content = src.read()

        with open(final_destination, "wb") as dst:
            dst.write(content)

        os.remove(source_path)
        print(f"✅ File moved to: {final_destination}")
    except OSError as e:
        print(f"❌ File operation failed: {e}")
