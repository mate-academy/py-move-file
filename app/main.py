import os


def move_file(command: str) -> None:
    # Split the command to extract source and destination
    _, src, dest = command.split()

    # Check if the destination ends with a slash (indicating a directory)
    if dest.endswith("/"):
        dest = os.path.join(dest, os.path.basename(src))

    # Manually check and create each directory in the destination path
    dest_dir = os.path.dirname(dest)
    current_path = ""
    for folder in dest_dir.split(os.sep):
        current_path = os.path.join(current_path, folder)
        if current_path and not os.path.exists(current_path):
            os.mkdir(current_path)

    # Copy the content of the source file to the destination
    with open(src, "r") as source_file, open(dest, "w") as dest_file:
        content = source_file.read()
        dest_file.write(content)

    # Remove the source file
    os.remove(src)
