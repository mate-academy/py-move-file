import os


def move_file(command: str) -> None:
    try:
        curr_command, source_file, output_file = command.split()
    except ValueError:
        raise ValueError("Not enough arguments")

    if curr_command != "mv":
        return

    dir_path = os.path.dirname(output_file)
    if not os.path.exists(output_file) and dir_path:
        os.makedirs(dir_path, exist_ok=True)

    with open(source_file, "r") as source, open(output_file, "w") as new_file:
        file_content = source.read()
        new_file.write(file_content)

    os.remove(source_file)
