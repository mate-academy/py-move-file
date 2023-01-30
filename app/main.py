import os


def move_file(command: str) -> None:
    if len(command.split()) == 3:
        input_command, source, destination = command.split()
        if input_command == "mv" and source != destination:
            path_to_file = os.path.split(destination)
            os.makedirs(path_to_file[0], exist_ok=True)
            with (
                 open(source, "r") as f_input,
                 open(destination, "w") as f_output
                 ):
                f_output.write(f_input.read())
            os.remove(source)
