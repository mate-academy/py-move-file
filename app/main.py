import os


def move_file(command: str) -> str:

    parts = command.split()

    if len(parts) < 3:
        return "Invalid command. Please provide source and destination paths."

    source_file = parts[1]
    destination = parts[2]

    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source_file))

    try:
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        os.rename(source_file, destination)
        return "File moved successfully."
    except Exception as e:
        return f"An error occurred: {str(e)}"
