import os


def move_file(command: str) -> None:
    parts = command.strip().split()

    # Validate basic command structure
    if len(parts) != 3 or parts[0] != "mv":
        return

    source, destination = parts[1], parts[2]

    # Check if source file exists
    if not os.path.exists(source):
        return

    # Abort if source and destination are the same
    if source == destination:
        return

    # If destination ends with '/', it's a directory path
    if destination.endswith("/"):
        print("Invalid: Destination ends with '/' and is missing file name.")
        return

    # Extract all directory parts from destination
    directory_path = os.path.dirname(destination)
    if directory_path:
        # Create nested directories if needed
        current = ""
        for part in directory_path.split("/"):
            current = os.path.join(current, part)
            if not os.path.exists(current):
                os.mkdir(current)

    # Copy content
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())

    # Remove original file
    os.remove(source)
