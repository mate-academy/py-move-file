import os


def move_file(command: str) -> None:
    current_command, source_file, destination_file = command.split()
    if current_command == "mv":
        root = os.path.split(destination_file)
        if root[0] != "":
            os.makedirs(root[0], exist_ok=True)

        with open(source_file) as first_file, \
                open(destination_file, "w") as result_file:
            data = first_file.read()
            result_file.write(data)
        os.remove(source_file)
