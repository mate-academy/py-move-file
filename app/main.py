import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        command, source, destination = command.split()
        if command == "mv" and source != destination:
            if os.path.dirname(destination):
                try:
                    os.makedirs(os.path.dirname(destination))
                except FileExistsError:
                    print("file path already created")
            if not os.path.split(destination)[-1]:
                destination += source
            with (
                open(source) as file_in,
                open(destination, "w") as file_out
            ):
                file_out.write(file_in.read())
            os.remove(source)
