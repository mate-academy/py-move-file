import os


def move_file(command: str) -> None:
    parts = command.split()
    if parts[0] != "mv" or len(parts) != 3:
        print("Invalid format!")
        return

    destination_path = parts[2]
    source_file = parts[1]

    """"якщо немає директорії призначення, створюємо її """
    dest_dir = os.path.dirname(destination_path)
    if dest_dir and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    try:
        os.rename(source_file, destination_path)
        print(f"File moved to {destination_path}")
    except Exception as e:
        print(f"Error: {e}")
