import os


def move_file(command: str) -> None:
    mode, source, destination = command.split()

    if os.path.dirname(destination):
        os.makedirs(os.path.dirname(destination), exist_ok=True)

        with open(source, "r") as file_in, open(destination, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
        os.remove(source)
    else:
        os.rename(source, destination)
