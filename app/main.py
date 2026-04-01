import os


def move_file(command: str) -> None:
    # Exclude input without the command "mv"
    if not command.startswith("mv "):
        print("The function only supports the 'mv' command!")
        return

    # Exclude the creation of a directory without a file.
    if command.endswith("/"):
        print("Specify the file name after '/'!")
        return

    instruction = command.split()
    first_file_name = instruction[1]
    dest_path = os.path.split(instruction[-1])[0]

    # If the original file needs to be copied to the same directory, rename it.
    if not dest_path:
        second_file_name = instruction[-1]
        os.rename(first_file_name, second_file_name)
    else:
        os.makedirs(dest_path, exist_ok=True)

        # Open source file for reading
        try:
            with open(first_file_name, "r") as source:
                content = source.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"[Errno 2] No such file or directory: '{first_file_name}'"
            )

        # Opening a new file for writing
        with open(instruction[-1], "w") as new_file:
            new_file.write(content)

        # Remove the original file
        os.remove(first_file_name)
