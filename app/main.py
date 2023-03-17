import os


def move_file(command: str) -> None:
    if len(command.split()) != 3:
        return

    cmd, source_file, final_file = command.split()

    if cmd == "mv":

        with open(source_file) as source:
            data = source.read()

        final_path, fin_file_name = os.path.split(final_file)

        if len(final_path) > 1:
            directory = final_path
        else:
            directory = "."

        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(os.path.join(directory, fin_file_name), "w") as target_file:
            target_file.write(data)

        os.remove(source_file)
