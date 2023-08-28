import os


def move_file(command: str) -> None:
    action, source, destination = command.split()

    if source == destination and action == "mv":
        return

    if "/" not in destination and action == "mv":
        os.rename(source, destination)
        return

    if destination.endswith("/"):
        destination = destination[:-1]
        new_file_name = source
    else:
        new_file_name = "".join(destination.split("/")[-1])
        destination = "/".join(destination.split("/")[:-1])

    if not os.path.exists(destination):
        os.makedirs(destination)

    destination += "/" + new_file_name
    with (
        open(source, "r") as old_file,
        open(destination, "w") as new_file
    ):
        content = old_file.read()
        new_file.write(content)

    os.remove(source)
