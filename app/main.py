import os


def move_file(command: str) -> None:
    command_arr = command.split()
    action = command_arr[0]
    source = command_arr[1]
    destination = command_arr[2]

    if source == destination and action == "mv":
        return

    if "/" not in destination and action == "mv":
        os.rename(source, destination)
        return

    if destination.endswith("/"):
        destination = destination[:-1]
        new_file_name = source
    else:
        destination = "/".join(command_arr[2].split("/")[:-1])
        new_file_name = "".join(command_arr[2].split("/")[-1])

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
