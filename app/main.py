import os


def move_file(command: str) -> None:
    cmd, source_file, final_file = command.split()

    if (
            len(command.split()) == 3
            and cmd == "mv"
            and final_file[-1] != "/"
    ):

        with open(source_file) as source:
            data = source.read()

        path, final_file_name = os.path.split(final_file)

        if len(path) > 1:
            directory = os.path.join(path)
        else:
            directory = "."

        if not os.path.exists(directory):
            os.makedirs(directory)

        new_file = os.path.join(directory, final_file_name)

        with open(new_file, "w") as copy:
            copy.write(data)

        os.remove(source_file)
