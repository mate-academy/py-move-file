import os


def move_file(command: str) -> None:
    command = command.split()

    if len(command) == 3 and command[0] == "mv":
        source_file, destination = command[1], command[2]
        end_path, end_file = os.path.split(destination)

        if end_path != "":
            end_path = end_path.split("/")
            directory = os.path.join(*end_path)
            if not os.path.exists(directory):
                os.makedirs(directory)

        full_end_path = os.path.join(*end_path, end_file)
        os.replace(source_file, full_end_path)
