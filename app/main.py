import os


def move_file(command: str) -> None:
    if not isinstance(command, str):
        return
    split_values = command.split(" ")
    if len(split_values) != 3:
        return
    elif split_values[1] == split_values[2]:
        return
    elif split_values[0] == "mv":
        if not os.path.isfile(split_values[1]):
            return
        destination = split_values[2]
        if destination.endswith(("/", os.sep)):
            target_dir = destination
            destination = os.path.join(destination,
                                       os.path.basename(split_values[1]))
        else:
            target_dir = os.path.dirname(destination)
        if target_dir:
            os.makedirs(target_dir, exist_ok=True)
        with open(split_values[1], "rb") as copy_file, \
                open(destination, "wb") as target_file:
            target_file.write(copy_file.read())
        os.remove(split_values[1])
