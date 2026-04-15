import os


def move_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "mv":
        return
    command_type, input_file, destination = command_parts

    dirs, output_file = os.path.split(destination)

    if not output_file:
        output_file = os.path.basename(input_file)
    if dirs:
        os.makedirs(dirs, exist_ok=True)
        output_file = os.path.join(dirs, output_file)

    try:
        with (
            open(input_file) as file_from,
            open(output_file, "w") as file_to
        ):
            file_to.write(file_from.read())
        os.remove(input_file)
    except FileNotFoundError:
        return
