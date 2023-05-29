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
    path = instruction[-1].split("/")[0:-1]
    source_path, second_file_name = os.path.split(command.split()[-1])
    file_path = os.path.join(os.path.join("/".join(path)), second_file_name)

    # If the original file needs to be copied to the same directory, rename it.
    if len(path) == 1:
        second_file_name = instruction[-1]
        os.rename(first_file_name, second_file_name)
    else:
        # create directories
        for i in range(len(path)):
            current_dir = os.path.join("/".join(path[:i + 1]))
            try:
                os.mkdir(current_dir)
            except FileExistsError:
                pass

        # Open source file for reading
        try:
            with open(first_file_name, "r") as source:
                content = source.read()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"[Errno 2] No such file or directory: '{first_file_name}'"
            )

        # Opening a new file for writing
        with open(file_path, "w") as new_file:
            new_file.write(content)

        # Remove the original file
        os.remove(first_file_name)
