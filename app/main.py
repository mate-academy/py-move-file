import os


def move_file(command: str) -> None:
    """
    Moves a file from one location to another,
    similar to the Linux `mv` command.

    Usage examples:
        move_file("mv file.txt new_file.txt")
        # Rename file
        move_file("mv file.txt dir1/dir2/file2.txt")
        # Move file into nested directories
        move_file("mv file.txt some_dir/")
        # Move file into directory (auto creates it)

    The function:
    - Creates all necessary directories if they don't exist.
    - Copies file content to the destination.
    - Removes the source file.
    - Prints operation results to the console.
    """

    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        print("Invalid command. Usage: mv <source> <destination>")
        return

    input_name, output_name = parts[1], parts[2]

    # Do nothing if source and destination are identical
    if input_name == output_name:
        print("Source and destination are the same. Nothing to do.")
        return

    # If destination ends with '/', treat it as directory
    if output_name[:-1] == "/":
        os.makedirs(output_name, exist_ok=True)
        output_name = output_name + input_name
    else:
        # Create parent directories if needed
        dir_path = os.path.dirname(output_name)
        if dir_path:
            os.makedirs(dir_path, exist_ok=True)

    try:
        with (open(input_name, "r") as input_file,
              open(output_name, "w") as output_file):
            for line in input_file:
                output_file.write(line)
        os.remove(input_name)
        print(f"Moved: '{input_name}' → '{output_name}'")
    except Exception as e:
        print(f"Error while moving '{input_name}' → '{output_name}': {e}")
