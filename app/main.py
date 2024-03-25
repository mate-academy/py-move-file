import os


def move_file(command: str) -> None:

    source, destination = command.split()[1:]

    source_parts = source.rsplit("/", 1)
    destination_parts = destination.rsplit("/", 1)

    if len(destination_parts) > 1:
        for path in destination_parts[:-1]:
            if not os.path.exists(path):
                os.makedirs(path)

    source_file = os.path.join(*source_parts)
    destination_file = os.path.join(*destination_parts)

    with open(source_file, "r") as file_in, \
            open(destination_file, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
    os.remove(source_file)
