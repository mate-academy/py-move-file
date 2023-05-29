import os


def move_file(command: str) -> None:
    # Exclude input without the command "mv"
    if command.split()[0] != "mv":
        print("The function only supports the 'mv' command!")
        return

    directories = command.split("/")

    # Exclude the creation of a directory without a file.
    if directories[-1] == "":
        print("Specify the file name after '/'!")
        return

    directory_names = [
        directories[direct].split()[-1]
        for direct in range(len(directories) - 1)
    ]
    first_file_name = directories[0].split()[1]
    second_file_name = directories[-1]
    directory_path = os.path.join("/".join(directory_names))
    file_path = os.path.join(directory_path, second_file_name)

    # If the original file needs to be copied to the same directory, rename it.
    if len(directories) == 1:
        second_file_name = directories[0].split()[-1]
        os.rename(first_file_name, second_file_name)
    else:
        # create directories
        for i in range(len(directory_names)):
            current_dir = os.path.join("/".join(directory_names[:i + 1]))
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
