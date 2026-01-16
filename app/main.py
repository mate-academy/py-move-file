import os


def move_file(command: str) -> None:
    try:
        command_to_run, source, destination = command.split(" ")
        if source == destination \
                or command_to_run != "mv":
            raise ValueError
    except ValueError:
        return None

    list_destination = os.path.dirname(destination)

    if list_destination == destination:
        os.remove(source, os.path.join(destination, source))

    if list_destination == "":
        os.rename(source, destination)
        return None

    if not os.path.exists(list_destination):
        os.makedirs(list_destination)

    with open(source, "r") as source_file, \
            open(destination, "w") as destination_file:
        content = source_file.read()
        destination_file.write(content)
    os.remove(source)
