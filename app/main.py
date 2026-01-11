import os


def move_file(text: str) -> None:
    command, from_file, to_file = text.split()

    if "/" in to_file:
        directory, file_name = os.path.split(to_file)
        directory += "/"
        os.makedirs(directory)
    else:
        os.rename(from_file, to_file)

    if command == "mv" and from_file != to_file:
        with open(from_file, "r") as file_in, open(to_file, "w") as to_file:
            to_file.write(file_in.read())

        os.remove(from_file)
