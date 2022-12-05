import os


def move_file(command: str) -> None:
    if command.startswith("mv") and not command.endswith("/"):
        command, initial_file, new_file = command.split()
        path, new_file_name = os.path.split(new_file)

        if path != "" and not os.path.exists(path):
            os.makedirs(path)

        with open(initial_file, "r") as file_in, \
                open(new_file, "w") as file_out:
            file_out.write(file_in.read())
            file_in.close()
            os.remove(initial_file)
